from textproof.typo import Typo
from textproof.api import api_query


class CheckedText:
    def __init__(self, text):
        self.text = text
        self.revised = text
        self.length_change = 0
        self.typos = [Typo(typo) for typo in api_query(text)]

    def __str__(self):
        return self.revised

    def fix_typos(self):
        for typo in self.typos:
            suggestion, offset, length, change = typo.select_fix()
            if suggestion:
                offset += self.length_change
                self.revised = "".join(
                    (
                        self.revised[:offset],
                        suggestion,
                        self.revised[offset + length:]
                    )
                )
                self.length_change += change
