from config_loader import load_targets
from logger import get_logger

from fetcher import fetch_url
from cleaner import clean_html
from extractor import extract_items


logger = get_logger()


def main():

    targets = load_targets()

    logger.info(
        f"Loaded {len(targets)} targets"
    )

    first_target = targets[0]

    logger.info(
        f"Testing: {first_target.name}"
    )

    result = fetch_url(
        first_target.url,
        first_target.timeout
    )

    if not result.success:

        logger.error(
            "Failed to fetch page"
        )

        return

    soup = clean_html(
        result.html
    )

    items = extract_items(
        soup,
        first_target.selector,
        first_target.name,
        first_target.url
    )

    logger.info(
        f"Extracted {len(items)} items"
    )

    for item in items[:10]:

        print()
        print(item.title)

        if item.url:
            print(item.url)


if __name__ == "__main__":
    main()