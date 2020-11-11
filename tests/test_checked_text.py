from test.conftest import fake_api_query
import pytest
import textproof.checked_text


class TestCheckedTest:

    @pytest.fixture
    def example_checked(self, monkeypatch, scope="class"):
        return textproof.checked_text.CheckedText(pytest.example_text)


    def test_checked_text_init(self, example_checked):
        assert example_checked.text == pytest.example_text
        assert len(example_checked.typos) == 3


    @pytest.mark.parametrize(
        "fake_inputs, expected",
        [((0, 0, 0), pytest.example_text), ((1, 1, 3), pytest.example_output)],
        indirect=["fake_inputs"]
    )
    def test_fix_typo(self, example_checked, fake_inputs, expected):
        example_checked.fix_typos()
        assert example_checked.revised == expected
