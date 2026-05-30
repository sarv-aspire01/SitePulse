from models.change_event import (
    ChangeEvent
)

from models.monitored_item import (
    MonitoredItem
)


def detect_changes(
    target_name: str,
    old_items: list[MonitoredItem],
    new_items: list[MonitoredItem]
) -> ChangeEvent:

    old_lookup = {}

    for item in old_items:

        key = (
            item.title,
            item.url
        )

        old_lookup[key] = item

    new_lookup = {}

    for item in new_items:

        key = (
            item.title,
            item.url
        )

        new_lookup[key] = item

    added_items = []

    for key in new_lookup:

        if key not in old_lookup:

            added_items.append(
                new_lookup[key]
            )

    removed_items = []

    for key in old_lookup:

        if key not in new_lookup:

            removed_items.append(
                old_lookup[key]
            )

    return ChangeEvent(
        target_name=target_name,
        added_items=added_items,
        removed_items=removed_items
    )