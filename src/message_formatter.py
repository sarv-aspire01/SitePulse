from datetime import datetime

from models.change_event import (
    ChangeEvent
)

from models.notification_message import (
    NotificationMessage
)


def build_change_notification(
    event: ChangeEvent,
    category: str,
    site_url: str
) -> NotificationMessage:

    lines = []

    lines.append(
        "CHANGE DETECTED"
    )

    lines.append("")

    lines.append(
        f"Target: {event.target_name}"
    )

    lines.append(
        f"Category: {category}"
    )

    lines.append("")

    if event.added_items:

        lines.append(
            f"Added ({len(event.added_items)}):"
        )

        lines.append("")

        for item in event.added_items:

            lines.append(
                f"• {item.title}"
            )

            if item.url:

                lines.append(
                    f"Direct Link: {item.url}"
                )

            lines.append("")

    if event.removed_items:

        lines.append(
            f"Removed ({len(event.removed_items)}):"
        )

        lines.append("")

        for item in event.removed_items:

            lines.append(
                f"• {item.title}"
            )

            if item.url:

                lines.append(
                    f"Direct Link: {item.url}"
                )

            lines.append("")

    lines.append(
        f"Main Site: {site_url}"
    )

    lines.append("")

    lines.append(
        "Detected:"
    )

    lines.append(
        datetime.utcnow().strftime(
            "%Y-%m-%d %H:%M UTC"
        )
    )

    return NotificationMessage(
        title=f"{event.target_name} Change",
        body="\n".join(lines),
        priority="high"
    )


def build_error_notification(
    target_name: str,
    site_url: str,
    error_message: str
) -> NotificationMessage:

    body = "\n".join(
        [
            "⚠ TARGET CHECK FAILED",
            "",
            f"Target: {target_name}",
            f"Main Site: {site_url}",
            "",
            f"Error: {error_message}",
            "",
            "Time:",
            datetime.utcnow().strftime(
                "%Y-%m-%d %H:%M UTC"
            )
        ]
    )

    return NotificationMessage(
        title=f"{target_name} Failed",
        body=body,
        priority="normal"
    )


def build_health_report(
    total_targets: int,
    successful_targets: int,
    failed_targets: list,
    changes_detected: int,
    runtime_seconds: float,
    suppressed_targets
) -> NotificationMessage:

    lines = []

    lines.append(
        "✅ SitePulse DAILY REPORT"
    )

    lines.append("")

    lines.append(
        f"Targets Checked: {total_targets}"
    )

    lines.append(
        f"Successful: {successful_targets}"
    )

    lines.append(
        f"Failed: {len(failed_targets)}"
    )

    lines.append(
        f"Changes Detected: {changes_detected}"
    )

    lines.append(
        f"Runtime: {runtime_seconds:.2f} seconds"
    )

    lines.append("")

    if failed_targets:

        lines.append(
            "Failed Targets:"
        )

        lines.append("")

        for name, url in failed_targets:

            lines.append(
                f"• {name}"
            )

            lines.append(
                f"  {url}"
            )

            lines.append("")
            
    if suppressed_targets:

        lines.append("")
        lines.append("🚫 Suppressed Targets:")
        lines.append("")

        for name, error, url in suppressed_targets:

            lines.append(f"• {name}")
            lines.append(f"  {url}")
            lines.append(f"  Last Error: {error}")
            lines.append("")

    return NotificationMessage(
        title="SitePulse Daily Report",
        body="\n".join(lines),
        priority="low"
    )
    