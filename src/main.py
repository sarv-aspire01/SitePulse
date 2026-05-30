from time import time

from config_loader import load_targets
from logger import get_logger

from fetcher import fetch_url
from cleaner import clean_html
from extractor import extract_items

from storage import load_snapshot, save_snapshot
from detector import detect_changes

from message_formatter import (
    build_change_notification,
    build_error_notification,
    build_health_report
)

from notifier import send_notification

from suppression import (
    load_state,
    save_state,
    record_failure,
    should_suppress,
    suppress_target,
    is_suppressed,
    reset_target
)

from models.notification_message import NotificationMessage


logger = get_logger()


def main():

    start_time = time()

    logger.info("Starting SitePulse...")

    targets = load_targets()

    state = load_state()

    total_targets = len(targets)
    successful_targets = 0
    failed_targets = []
    changes_detected = 0

    logger.info(f"Loaded {total_targets} targets")

    for target in targets:

        logger.info(f"Checking {target.name}")

        result = fetch_url(target.url, target.timeout)

        # -----------------------------
        # FAILURE HANDLING
        # -----------------------------
        if not result.success:

            logger.warning(
                f"{target.name} failed "
                f"(status={result.status_code}) "
                f"{result.error_message}"
            )

            state = record_failure(
                state,
                target.name,
                result.error_message
            )
            state[target.name]["url"] = target.url

            # ACTIVE FAILURE (NOT SUPPRESSED)
            if not is_suppressed(state, target.name):

                failed_targets.append(
                    (target.name, target.url)
                )

                try:

                    notification = build_error_notification(
                        target.name,
                        target.url,
                        str(result.error_message)
                    )

                    send_notification(notification)

                except Exception as e:
                    logger.error(f"Error notification failed: {e}")

                # CHECK IF SHOULD ENTER SUPPRESSION
                if should_suppress(
                    state,
                    target.name,
                    target.retries
                ):
                    state = suppress_target(
                        state,
                        target.name
                    )

            save_state(state)
            continue

        # -----------------------------
        # SUCCESS PATH
        # -----------------------------
        successful_targets += 1

        logger.info(
            f"{target.name}: "
            f"status={result.status_code} "
            f"time={result.response_time:.2f}s"
        )

        soup = clean_html(result.html)

        items = extract_items(
            soup,
            target.selector,
            target.name,
            target.url
        )

        old_items = load_snapshot(target.name)

        if not old_items:

            logger.info(
                f"{target.name}: Creating baseline snapshot"
            )

            save_snapshot(target.name, items)
            continue

        event = detect_changes(
            target.name,
            old_items,
            items
        )

        if event.added_items or event.removed_items:

            changes_detected += 1

            logger.info(f"{target.name}: Changes detected")

            notification = build_change_notification(
                event,
                target.category,
                target.url
            )

            try:
                send_notification(notification)
            except Exception as e:
                logger.error(f"Notification failed: {e}")

        # -----------------------------
        # RECOVERY FROM SUPPRESSION
        # -----------------------------
        if is_suppressed(state, target.name):

            logger.info(
                f"{target.name} recovered from suppression"
            )

            recovery_msg = NotificationMessage(
                title="RECOVERY DETECTED",
                body=f"{target.name} is back online",
                priority="normal"
            )

            send_notification(recovery_msg)

            reset_target(state, target.name)

        save_snapshot(target.name, items)

    # -----------------------------
    # DAILY HEALTH REPORT
    # -----------------------------
    runtime_seconds = time() - start_time

    suppressed_targets = [
        (name, data.get("last_error", ""), target_url)
        for name, data in state.items()
        for target_url in [data.get("url", "unknown")]
        if data.get("suppressed")
    ]

    report = build_health_report(
        total_targets=total_targets,
        successful_targets=successful_targets,
        failed_targets=failed_targets,
        changes_detected=changes_detected,
        runtime_seconds=runtime_seconds,
        suppressed_targets=suppressed_targets
    )

    try:
        send_notification(report)
    except Exception as e:
        logger.error(f"Health report failed: {e}")

    save_state(state)


if __name__ == "__main__":
    main()