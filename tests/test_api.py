import pytest
import requests
from requests import Response

from .conftest import example_api_response, example_text


def test_api_layout() -> None:
    response: Response = requests.post(
        "https://api.languagetool.org/v2/check",
        headers={"Content-Type": "application/json"},
        data={"text": example_text, "language": "en-US"},
    )
    if response.status_code != 200:
        pytest.skip("Server unavailable")

    matches = response.json()["matches"]
    for from_api, expected in zip(matches, example_api_response):
        from_api_set: set[str] = set(from_api.keys())
        expected_set: set[str] = set(expected.keys())
        assert expected_set.issubset(from_api_set)
