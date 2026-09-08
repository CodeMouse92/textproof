from typing import TypedDict, NotRequired, cast
import requests

class RawTypoContext(TypedDict):
    length: int
    offset: int
    text: str

class RawTypoSuggestion(TypedDict):
    shortDescription: NotRequired[str]
    value: str

class RawTypo(TypedDict):
    context: RawTypoContext
    length: int
    message: str
    offset: int
    replacements: list[RawTypoSuggestion]


def api_query(text: str) -> list[RawTypo]:
    lang: str = "en-US"
    response: requests.Response = requests.post(
        "https://api.languagetool.org/v2/check",
        headers={"Content-Type": "application/json"},
        data={"text": text, "language": lang},
    )
    if response.status_code != 200:
        raise RuntimeError(f"API error: [{response}] {response.text}")

    software: dict[str, str] = response.json()["software"]
    print(f"{software['name']} v{software['version']}")
    print(response.json()['language']['name'])
    return cast(list[RawTypo], response.json()["matches"])
