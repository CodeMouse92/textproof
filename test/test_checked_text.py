import pytest
from textproof.checked_text import CheckedText
from . import dummy


@pytest.fixture
def example_checked(fake_api_query):
    return CheckedText(dummy.text)


def test_checked_text_init(example_checked,):
    assert example_checked.text == dummy.text
    assert len(example_checked.typos) == 3


@pytest.mark.parametrize("inputs, expected", [((0, 0, 0), dummy.text), ((1, 1, 3), dummy.output)])
def test_fix_typo(example_checked, monkeypatch, inputs, expected):
    monkeypatch.setattr('builtins.input', dummy.fake_input(inputs))
    example_checked.fix_typos()
    assert example_checked.revised == expected
