import requests


def api_query(text):
    response = requests.post(
        "https://languagetool.org/api/v2/check",
        headers={"Content-Type": "application/json"},
        data={"text": text, "language": "en-US"},
    )
    if response.status_code == 200:
        software = response.json()["software"]
        print(f"{software['name']} v{software['version']}")
        print(f"{response.json()['language']['name']}")
        return response.json()["matches"]
    else:
        raise RuntimeError(f"API error: [{response}] {response.text}")


def dummy_api_query(text):
    return [
        {
            'context': {
                'length': 2,
                'offset': 7,
                'text': 'He and me went too the stor.'
            },
            'length': 2,
            'message': 'Did you mean “I”?',
            'offset': 7,
            'replacements': [{'value': 'I'}],
        },
        {
            'context': {'length': 7,
                    'offset': 15,
                    'text': 'He and me went too the stor.'},
            'length': 7,
            'message': 'Did you mean “to the”?',
            'offset': 15,
            'replacements': [{'value': 'to the'}],
        },
        {
            'context': {
                'length': 4,
                'offset': 23,
                'text': 'He and me went too the stor.'
            },
            'length': 4,
            'message': 'Possible spelling mistake found.',
            'offset': 23,
            'replacements': [{'value': 'story'},
                            {'value': 'stop'},
                            {'value': 'store'},
                            {'value': 'storm'}]
        }
    ]
