from config_loader import load_targets
from logger import get_logger


logger = get_logger()


def main():

    logger.info(
        "Starting SitePulse..."
    )

    targets = load_targets()

    logger.info(
        f"Loaded {len(targets)} targets"
    )

    print()

    for target in targets:
        print(f"✓ {target.name}")

    print()
    print("Configuration valid")


if __name__ == "__main__":
    main()