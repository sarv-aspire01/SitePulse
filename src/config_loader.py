from pathlib import Path

import yaml

from models.target import Target


CONFIG_DIR = Path("config")


def validate_target(target_data: dict):

    required_fields = [
        "name",
        "category",
        "url",
        "selector"
    ]

    for field in required_fields:

        if field not in target_data:
            raise ValueError(
                f"Missing required field: {field}"
            )

    if not target_data["url"].startswith(
        ("http://", "https://")
    ):
        raise ValueError(
            f"Invalid URL: {target_data['url']}"
        )


def load_targets():

    targets = []

    yaml_files = CONFIG_DIR.glob("*.yaml")

    for yaml_file in yaml_files:

        with open(
            yaml_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = yaml.safe_load(f)

        if not data:
            continue

        for target_data in data.get(
            "targets",
            []
        ):

            validate_target(
                target_data
            )

            target = Target(
                name=target_data["name"],
                category=target_data["category"],
                url=target_data["url"],
                selector=target_data["selector"],
                timeout=target_data.get(
                    "timeout",
                    30
                ),
                retries=target_data.get(
                    "retries",
                    3
                ),
                severity=target_data.get(
                    "severity",
                    "medium"
                ),
                extraction_type=target_data.get(
                    "extraction_type",
                    "links"
                )
            )

            targets.append(target)

    return targets