from dataclasses import dataclass, field
from typing import List


@dataclass
class ChangeEvent:
    target_name: str
    added_items: List[str] = field(default_factory=list)
    removed_items: List[str] = field(default_factory=list)
    timestamp: str = ""