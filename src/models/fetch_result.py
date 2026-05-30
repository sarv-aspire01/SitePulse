from dataclasses import dataclass


@dataclass
class FetchResult:
    html: str
    status_code: int
    response_time: float
    success: bool
    error_message: str = ""