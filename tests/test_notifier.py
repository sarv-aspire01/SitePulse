from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent / "src"
    )
)

from models.notification_message import (
    NotificationMessage
)

from notifier import (
    send_notification
)


notification = NotificationMessage(
    title="SitePulse Test",
    body="Notification pipeline operational.",
    priority="high"
)

print(
    send_notification(
        notification
    )
)