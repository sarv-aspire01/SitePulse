import requests

from models.fetch_result import FetchResult


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
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
            success=response.ok,
            error_message=""
        )

    except Exception as e:

        return FetchResult(
            html="",
            status_code=0,
            response_time=0,
            success=False,
            error_message=str(e)
        )