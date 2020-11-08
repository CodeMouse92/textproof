from textproof.checked_text import CheckedText


def main():
    check = None
    while True:
        text = input("Enter a sentence to check, or 'q' to exit...\n> ")
        if text == '':
            continue
        elif check and text == 'r':
            text = str(check)
        elif text == 'q':
            break

        check = CheckedText(text)
        check.fix_typos()

        print("\nREVISED:", check)

        print("\nEnter 'r' to recheck revised text.")

    print("Goodbye.")


if __name__ == "__main__":
    main()
