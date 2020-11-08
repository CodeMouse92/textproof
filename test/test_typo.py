import pytest
from textproof.typo import Typo
from . import dummy


# TODO: Resume from here. See and achieve https://docs.pytest.org/en/stable/example/parametrize.html?highlight=indirect#indirect-parametrization-with-multiple-fixtures

@pytest.fixture
def example_typo():
    return Typo(dummy.api_response[i])


@pytest.fixture
def example_prompt():
    return dummy.prompts[i]


@pytest.mark.parametrize("example_typo", range(2), indirect=True)
def test_create_typo(example_typo):
    typo, _ = example_typo
    assert typo.offset == 23
    assert typo.length == 4
    assert typo.message == 'Possible spelling mistake found.'
    assert typo.suggestions == typo['replacements']


@pytest.mark.parametrize("example_typo", (2,), indirect=True)
def test_choice(example_typo, monkeypatch):
    typo, _ = example_typo
    monkeypatch.setattr('builtins.input', dummy.fake_input((-1, 5, 3)))
    assert typo.get_choice() == 3


@pytest.mark.parametrize("example_typo", range(2), indirect=True)
def test_prompt(example_typo, capsys, monkeypatch):
    typo, prompt = example_typo
    monkeypatch.setattr('builtins.input', lambda _: '0')
    typo.select_fix()
    captured = capsys.readouterr()
    assert captured.out == prompt
