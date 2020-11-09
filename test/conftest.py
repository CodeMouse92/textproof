import pytest
from . import dummy


@pytest.fixture
def example_response(request):
    marker = request.node.get_closest_marker("typo_id")
    if marker is None:
        i = 1
    else:
        i = marker.args[0]
    return dummy.api_response[i]


@pytest.fixture
def example_typo(request):
    from textproof.typo import Typo

    marker = request.node.get_closest_marker("typo_id")
    if marker is None:
        i = 1
    else:
        i = marker.args[0]
    return Typo(dummy.api_response[i])


@pytest.fixture
def example_prompt(request):
    marker = request.node.get_closest_marker("typo_id")
    if marker is None:
        i = 1
    else:
        i = marker.args[0]
    return dummy.prompts[i]


@pytest.fixture
def fake_api_query(monkeypatch):
    def api_query(_):
        return dummy.api_response
    monkeypatch.setattr('textproof.api.api_query', api_query)
