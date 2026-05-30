from dataclasses import dataclass


@dataclass
class Target:
    name: str
    category: str
    url: str
    selector: str
    timeout: int = 30
    retries: int = 3
    severity: str = "medium"