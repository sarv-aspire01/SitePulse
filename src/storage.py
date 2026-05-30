import json
from pathlib import Path

from models.monitored_item import MonitoredItem

SNAPSHOT_DIR = Path(
    "data/snapshots"
)

SNAPSHOT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def snapshot_path(
    target_name: str
) -> Path:

    safe_name = (
        target_name
        .replace(" ", "_")
        .lower()
    )

    return (
        SNAPSHOT_DIR /
        f"{safe_name}.json"
    )

#  save snapshot


def save_snapshot(
    target_name: str,
    items: list[MonitoredItem]
):

    path = snapshot_path(
        target_name
    )

    data = []

    for item in items:

        data.append(
            {
                "title": item.title,
                "url": item.url,
                "content": item.content,
                "source_target": item.source_target
            }
        )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False
        )

# load snapshot

def load_snapshot(
    target_name: str
):

    path = snapshot_path(
        target_name
    )

    if not path.exists():

        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    items = []

    for item in data:

        items.append(
            MonitoredItem(
                title=item["title"],
                url=item["url"],
                content=item["content"],
                source_target=item.get(
                    "source_target",
                    ""
                )
            )
        )

    return items