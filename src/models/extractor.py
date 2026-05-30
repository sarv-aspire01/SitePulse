from urllib.parse import urljoin

from models.monitored_item import (
    MonitoredItem
)


def extract_items(
    soup,
    selector,
    source_target,
    base_url
):

    items = []

    elements = soup.select(selector)

    for element in elements:

        title = element.get_text(
            strip=True
        )

        if not title:
            continue

        href = element.get(
            "href",
            ""
        )

        full_url = urljoin(
            base_url,
            href
        )

        items.append(
            MonitoredItem(
                title=title,
                url=full_url,
                content=title,
                source_target=source_target
            )
        )

    return items