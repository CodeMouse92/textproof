#!/usr/bin/env python3

import click
from textproof.fileio import FileIO
from textproof.checked_text import CheckedText

@click.command()
@click.argument('path')
@click.option('--output', default=None, help="the path to write to")
def main(path, output):
    file = FileIO(path, output)
    try:
        file.load()
    except FileNotFoundError:
        print(f"Could not open file {path}")
        return

    check = CheckedText(file.data)
    check.fix_typos()
    file.data = str(check)

    file.save()

    # import cProfile, pstats
    # with cProfile.Profile() as pr:
    #     file = FileIO(path, output)
    #     try:
    #         file.load()
    #     except FileNotFoundError:
    #         print(f"Could not open file {path}")
    #         return

    #     check = CheckedText(file.data)
    #     check.fix_typos()
    #     file.data = str(check)

    #     file.save()
    # stats = pstats.Stats(pr)
    # stats.strip_dirs()
    # stats.sort_stats(pstats.SortKey.CUMULATIVE)
    # stats.print_stats(10)


if __name__ == "__main__":
    main()
