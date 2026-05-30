from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent / "src"
    )
)

from diff_generator import (
    generate_diff
)

from models.change_event import (
    ChangeEvent
)

from models.monitored_item import (
    MonitoredItem
)


event = ChangeEvent(
    target_name="Example"
)

event.added_items.append(
    MonitoredItem(
        title="Notice C",
        url="https://example.com/c",
        content=""
    )
)

event.removed_items.append(
    MonitoredItem(
        title="Notice B",
        url="https://example.com/b",
        content=""
    )
)

print(
    generate_diff(event)
)