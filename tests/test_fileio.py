import pytest
from pathlib import Path
from textproof.fileio import FileIO


class TestFileIO:
    demo_data: str = "To be, or not to be, that is the question!"

    @pytest.fixture
    def demo_in_file(self, tmp_path: str) -> str:
        test_in_file: Path = Path(tmp_path) / 'to_be.txt'
        with test_in_file.open('w') as file:
            file.write(self.demo_data)
        return str(test_in_file)

    @pytest.fixture
    def demo_out_file(self, tmp_path: str) -> str:
        test_out_file: Path = Path(tmp_path) / 'out.txt'
        return str(test_out_file)

    def test_in_path(self, demo_in_file: str) -> None:
        file: FileIO = FileIO(demo_in_file)
        assert file.in_file == Path(demo_in_file)

    def test_out_path(self, demo_in_file: str, demo_out_file: str) -> None:
        file: FileIO = FileIO(demo_in_file, demo_out_file)
        assert file.out_file == Path(demo_out_file)

    def test_no_out_path(self, demo_in_file: str) -> None:
        file: FileIO = FileIO(demo_in_file)
        assert file.in_file == file.out_file

    def test_invalid_in_path(self) -> None:
        with pytest.raises(FileNotFoundError):
            FileIO('tests/idonotexist.txt')

    def test_load(self, demo_in_file: str) -> None:
        file: FileIO = FileIO(demo_in_file)
        file.load()
        assert file.data == self.demo_data

    def test_save(self, demo_in_file: str, demo_out_file: str) -> None:
        file: FileIO = FileIO(demo_in_file, demo_out_file)
        file.data = self.demo_data
        file.save()
        with Path(demo_out_file).open('r') as check_file:
            assert check_file.read() == self.demo_data

    def test_save_no_load(self, demo_in_file: str, demo_out_file: str) -> None:
        file: FileIO = FileIO(demo_in_file, demo_out_file)
        with pytest.raises(RuntimeError):
            file.save()
