import pytest
from textproof.checked_text import CheckedText


class TestCheckedText:

    @pytest.fixture
    def example_checked(self, monkeypatch):
        return CheckedText(pytest.example_text)

    def test_checked_text__init(self, example_checked):
        assert example_checked.text == pytest.example_text
        assert len(example_checked.typos) == 3

    @pytest.mark.parametrize(
        ("fake_inputs", "expected"),
        [
            ((0, 0, 0), pytest.example_text),
            ((1, 1, 3), pytest.example_output)
        ],
        indirect=["fake_inputs"]
    )
    def test_fix_typo(self, example_checked, fake_inputs, expected):
        example_checked.fix_typos()
        assert example_checked.revised == expected
