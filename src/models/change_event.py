from dataclasses import (
    dataclass,
    field
)

from typing import List

from models.monitored_item import (
    MonitoredItem
)


@dataclass
class ChangeEvent:

    target_name: str

    added_items: List[
        MonitoredItem
    ] = field(
        default_factory=list
    )

    removed_items: List[
        MonitoredItem
    ] = field(
        default_factory=list
    )

    timestamp: str = ""