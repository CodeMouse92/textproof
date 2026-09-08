from typing import override

from textproof.api import RawTypo, RawTypoSuggestion

type Fix_T = tuple[str | None, int, int, int]


class Typo:
    def __init__(self, typo: RawTypo) -> None:
        context = typo["context"]
        self.text: str = context["text"]
        self.hint_offset: int = int(context["offset"])
        self.offset: int = int(typo["offset"])
        self.length: int = int(typo["length"])
        self.message: str = typo["message"]
        self.suggestions: list[RawTypoSuggestion] = typo["replacements"]

    @override
    def __str__(self) -> str:
        underline: str = "".join((" " * self.hint_offset, "^" * self.length))
        return "\n".join((self.text, underline, self.message))

    def get_choice(self) -> int:
        while True:
            raw: str = input("Select an option: ")
            try:
                choice: int = int(raw)
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if choice < 0 or choice > len(self.suggestions):
                print("Invalid choice.")
                continue

            return choice

    def select_fix(self) -> Fix_T:
        print('')
        print(self)

        for num, suggestion in enumerate(self.suggestions, 1):
            if "shortDescription" in suggestion:
                print(
                    f"{num}: {suggestion['value']} "
                    f"({suggestion['shortDescription']})"
                )
            else:
                print(f"{num}: {suggestion['value']}")
        print("0: (Skip)")

        choice: int = self.get_choice()
        if choice > 0:
            suggestion_text: str = self.suggestions[choice - 1]["value"]
            length_change = len(suggestion_text) - self.length
            return (suggestion_text, self.offset, self.length, length_change)
        else:
            return (None, 0, 0, 0)
