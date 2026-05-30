from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent / "src"
    )
)

from storage import (
    save_snapshot,
    load_snapshot
)

from models.monitored_item import (
    MonitoredItem
)


def main():

    item = MonitoredItem(
        title="Test Notice",
        url="https://example.com",
        content="Test Notice Content",
        source_target="Example"
    )

    save_snapshot(
        "Example",
        [item]
    )

    loaded_items = load_snapshot(
        "Example"
    )

    print(
        f"Loaded {len(loaded_items)} item(s)"
    )

    for item in loaded_items:

        print(
            item.title
        )

        print(
            item.url
        )


if __name__ == "__main__":
    main()