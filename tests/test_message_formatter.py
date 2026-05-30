from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent / "src"
    )
)

from models.change_event import (
    ChangeEvent
)

from models.monitored_item import (
    MonitoredItem
)

from message_formatter import (
    build_change_notification
)


event = ChangeEvent(
    target_name="UPSC Notifications"
)

event.added_items.append(
    MonitoredItem(
        title="Engineering Services Exam 2026",
        url="https://upsc.gov.in/test",
        content=""
    )
)

notification = (
    build_change_notification(
        event,
        "Government",
        "https://upsc.gov.in"
    )
)

print(notification.title)

print()

print(notification.body)