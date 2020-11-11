import requests


def api_query(text):
    url = "https://languagetool.org/api/v2/check",
    lang = "en-US"
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data={"text": text, "language": lang},
    )
    if response.status_code == 200:
        software = response.json()["software"]
        print(f"{software['name']} v{software['version']}")
        print(f"{url}")
        print(f"{response.json()['language']['name']}")
        return response.json()["matches"]
    else:
        raise RuntimeError(f"API error: [{response}] {response.text}")
