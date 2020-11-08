class Typo:
    def __init__(self, typo):
        context = typo["context"]
        self.text = context["text"]
        self.offset = int(context["offset"])
        self.length = int(context["length"])
        self.message = typo["message"]
        self.suggestions = typo["replacements"]

    def __str__(self):
        underline = "".join((" " * self.offset, "^" * self.length))
        return "\n".join((self.text, underline, self.message))

    def get_choice(self):
        while True:
            raw = input("Select an option: ")
            try:
                choice = int(raw)
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if choice < 0 or choice > len(self.suggestions):
                print("Invalid choice.")
                continue

            return choice

    def select_fix(self):
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

        choice = self.get_choice()
        if choice > 0:
            suggestion = self.suggestions[choice - 1]["value"]
            length_change = len(suggestion) - self.length
            return (suggestion, self.offset, self.length, length_change)
        else:
            return (None, 0, 0, 0)
