from bs4 import BeautifulSoup


def clean_html(
    html: str
) -> BeautifulSoup:

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    for tag in soup(
        ["script", "style", "noscript"]
    ):
        tag.decompose()

    return soup