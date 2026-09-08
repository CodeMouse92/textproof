from pathlib import Path


class FileIO:

    def __init__(self, in_file: str, out_file: str | None = None) -> None:
        self.in_file: Path = Path(in_file)
        if not self.in_file.exists():
            raise FileNotFoundError(f"Invalid input file: {self.in_file}")

        if out_file is None:
            out_file = in_file
        self.out_file: Path = Path(out_file)
        self.out_file_tmp: Path = Path(out_file + '.tmp')

        self.data: str = ''

    def load(self) -> str:
        if not self.data:
            with self.in_file.open('r') as file:
                self.data = file.read()

        return self.data

    def save(self) -> None:
        if not self.data:
            raise RuntimeError("Nothing to save.")

        with self.out_file_tmp.open('w') as file:
            file.write(self.data)
        self.out_file_tmp.rename(self.out_file)
