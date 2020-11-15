import pytest
from textproof.typo import Typo


class TestTypo:

    @pytest.mark.parametrize(
        ("example_typo", "example_response"),
        [(0, 0), (1, 1), (2, 2)],
        indirect=("example_typo", "example_response")
    )
    def test_create_typo(self, example_typo, example_response):
        assert example_typo.offset == example_response['offset']
        assert example_typo.length == example_response['length']
        assert example_typo.message == example_response['message']
        assert example_typo.suggestions == example_response['replacements']

    @pytest.mark.typo_id(2)
    @pytest.mark.parametrize(
        ("fake_inputs"),
        [('-1', '20', '3'), '3', ('fish', '1.1', '3')],
        indirect=True
    )
    def test_choice(self, example_typo, fake_inputs):
        assert example_typo.get_choice() == 3

    @pytest.mark.parametrize(
        "example_typo, example_prompt",
        [(n, n) for n in range(2)],
        indirect=["example_typo", "example_prompt"]
    )
    def test_prompt(self, example_typo, example_prompt, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '0')
        example_typo.select_fix()
        captured = capsys.readouterr()
        assert captured.out == example_prompt
