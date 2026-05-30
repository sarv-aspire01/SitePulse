from dataclasses import dataclass


@dataclass
class MonitoredItem:
    title: str
    url: str
    content: str = ""