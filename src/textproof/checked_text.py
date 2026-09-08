from typing import override

from textproof.typo import Typo
from textproof.api import api_query


class CheckedText:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.revised: str = text
        self.length_change: int = 0
        self.typos: list[Typo] = [
            Typo(typo) for typo in api_query(text)
        ]

    @override
    def __str__(self) -> str:
        return self.revised

    def fix_typos(self) -> None:
        for typo in self.typos:
            suggestion, offset, length, change = (
                typo.select_fix())
            if not suggestion:
                continue
            offset += self.length_change
            self.revised = "".join(
                (
                    self.revised[:offset],
                    suggestion,
                    self.revised[offset + length:]
                )
            )
            self.length_change += change
