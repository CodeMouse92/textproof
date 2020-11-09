import pytest
from textproof.typo import Typo
from . import dummy


@pytest.mark.parametrize("example_typo", range(3), indirect=True)
@pytest.mark.parametrize("example_response", range(3), indirect=True)
def test_create_typo(example_typo, example_response):
    assert example_typo.offset == example_response['offset']
    assert example_typo.length == example_response['length']
    assert example_typo.message == example_response['message']
    assert example_typo.suggestions == example_response['replacements']


@pytest.mark.typo_id(2)
def test_choice(example_typo, monkeypatch):
    monkeypatch.setattr('builtins.input', dummy.fake_input((-1, 5, 3)))
    assert example_typo.get_choice() == 3


@pytest.mark.parametrize("example_typo", range(3), indirect=True)
@pytest.mark.parametrize("example_prompt", range(3), indirect=True)
def test_prompt(example_typo, example_prompt, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '0')
    example_typo.select_fix()
    captured = capsys.readouterr()
    assert captured.out == example_prompt
