from config_loader import load_targets
from logger import get_logger

from fetcher import fetch_url
from cleaner import clean_html
from extractor import extract_items


logger = get_logger()


def main():

    logger.info(
        "Starting WatchTower..."
    )

    targets = load_targets()

    logger.info(
        f"Loaded {len(targets)} targets"
    )

    for target in targets:

        logger.info(
            f"Checking {target.name}"
        )

        result = fetch_url(
            target.url,
            target.timeout
        )

        if not result.success:

            logger.warning(
                f"{target.name} failed "
                f"(status={result.status_code}) "
                f"{result.error_message}"
            )

            continue

        soup = clean_html(
            result.html
        )

        items = extract_items(
            soup,
            target.selector,
            target.name,
            target.url
        )

        logger.info(
            f"{target.name}: "
            f"{len(items)} items extracted"
        )

        for item in items[:5]:

            print("\n---")
            print(
                f"Title: {item.title}"
            )
            print(
                f"URL: {item.url}"
            )


if __name__ == "__main__":
    main()