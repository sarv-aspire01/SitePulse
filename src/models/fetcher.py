import requests
from models.fetch_result import FetchResult


DEFAULT_HEADERS = {
    "User-Agent": (
        "WatchTower/1.0 "
        "(GitHub Actions Monitoring Bot)"
    )
}


def fetch_url(
    url: str,
    timeout: int = 30
) -> FetchResult:

    try:

        response = requests.get(
            url,
            headers=DEFAULT_HEADERS,
            timeout=timeout
        )

        return FetchResult(
            html=response.text,
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds(),
            success=response.ok
        )

    except requests.RequestException:

        return FetchResult(
            html="",
            status_code=0,
            response_time=0,
            success=False
        )