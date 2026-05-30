from dataclasses import dataclass


@dataclass
class NotificationMessage:

    title: str

    body: str

    priority: str = "normal"