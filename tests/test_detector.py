from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent / "src"
    )
)

from detector import detect_changes

from models.monitored_item import (
    MonitoredItem
)

old_items = [

    MonitoredItem(
        title="Notice A",
        url="a",
        content=""
    ),

    MonitoredItem(
        title="Notice B",
        url="b",
        content=""
    )
]


new_items = [

    MonitoredItem(
        title="Notice A",
        url="a",
        content=""
    ),

    MonitoredItem(
        title="Notice C",
        url="c",
        content=""
    )
]

event = detect_changes(
    "Example",
    old_items,
    new_items
)


print(
    len(event.added_items)
)

print(
    len(event.removed_items)
)

