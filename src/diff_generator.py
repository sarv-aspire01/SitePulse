from models.change_event import (
    ChangeEvent
)


def generate_diff(
    event: ChangeEvent
) -> str:

    lines = []

    lines.append(
        f"Target: {event.target_name}"
    )

    lines.append("")

    if event.added_items:

        lines.append(
            f"Added ({len(event.added_items)}):"
        )

        for item in event.added_items:

            lines.append(
                f"+ {item.title}"
            )

            if item.url:

                lines.append(
                    f"  {item.url}"
                )

        lines.append("")

    if event.removed_items:

        lines.append(
            f"Removed ({len(event.removed_items)}):"
        )

        for item in event.removed_items:

            lines.append(
                f"- {item.title}"
            )

            if item.url:

                lines.append(
                    f"  {item.url}"
                )

        lines.append("")

    if (
        not event.added_items
        and
        not event.removed_items
    ):

        lines.append(
            "No changes detected."
        )

    return "\n".join(lines)