import pytest
from pytest import MonkeyPatch

from .conftest import example_output, example_text
from textproof.checked_text import CheckedText


class TestCheckedText:

    @pytest.fixture
    def example_checked(self, monkeypatch: MonkeyPatch) -> CheckedText:
        return CheckedText(example_text)

    def test_checked_text__init(self, example_checked: CheckedText) -> None:
        assert example_checked.text == example_text
        assert len(example_checked.typos) == 3

    @pytest.mark.parametrize(
        ("fake_inputs", "expected"),
        [
            ((0, 0, 0), example_text),
            ((1, 1, 3), example_output)
        ],
        indirect=["fake_inputs"]
    )
    def test_fix_typo(self, example_checked: CheckedText, fake_inputs: tuple[tuple[int, int, int], str], expected: str) -> None:
        example_checked.fix_typos()
        assert example_checked.revised == expected
