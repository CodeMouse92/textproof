import pytest

example_text = "He and me went too the stor."

example_output = "He and I went to the store."

example_api_response = [
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


example_prompts = [
"""
He and me went too the stor.
       ^^
Did you mean “I”?
1: I
0: (Skip)
""",
"""
He and me went too the stor.
               ^^^^^^^
Did you mean “to the”?
1: to the
0: (Skip)
""",
"""
He and me went too the stor.
                       ^^^^
Possible spelling mistake found.
1: story
2: stop
3: store
4: storm
0: (Skip)
"""
]

def pytest_configure(config):
    pytest.example_text = example_text
    pytest.example_output = example_output
    pytest.example_api_response = example_api_response
    pytest.example_prompts = example_prompts


@pytest.fixture
def example_response(request):
    marker = request.node.get_closest_marker("typo_id")
    if marker:
        index = marker.args[0]
    else:
        index = request.param
    return example_api_response[index]


@pytest.fixture
def example_typo(request):
    marker = request.node.get_closest_marker("typo_id")
    if marker:
        index = marker.args[0]
    else:
        index = request.param

    from textproof.typo import Typo
    return Typo(example_api_response[index])


@pytest.fixture
def fake_inputs(request, monkeypatch):
    def fake():
        value = iter(request.param)

        def input(_):
            return next(value)

        return input

    monkeypatch.setattr('builtins.input', fake())


@pytest.fixture
def example_prompt(request):
    marker = request.node.get_closest_marker("typo_id")
    if marker:
        index = marker.args[0]
    else:
        index = request.param

    return example_prompts[index]


@pytest.fixture(autouse=True)
def fake_api_query(monkeypatch):
    def mock_api_query(_):
        print("FAKING IT")
        return example_api_response

    monkeypatch.setattr('textproof.api.api_query', mock_api_query)
    monkeypatch.setattr('textproof.checked_text.api_query', mock_api_query)
