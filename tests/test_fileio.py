import pytest
import pathlib
import textwrap
from textproof.fileio import FileIO


class TestFileIO:

    test_data = textwrap.dedent("""\
        To be, or not to be, that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune,
        Or to take Arms against a Sea of troubles,
        And by opposing end them: to die, to sleep;
        No more; and by a sleep, to say we end
        The heart-ache, and the thousand natural shocks
        """)

    def test_in_path(self):
        file = FileIO('test/to_be.txt')
        assert file.in_file == pathlib.Path('test/to_be.txt')

    def test_out_path(self):
        file = FileIO('test/to_be.txt', 'test/out.txt')
        assert file.out_file == pathlib.Path('test/out.txt')

    def test_no_out_path(self):
        file = FileIO('test/to_be.txt')
        assert file.in_file == file.out_file

    def test_invalid_in_path(self):
        with pytest.raises(FileNotFoundError):
            FileIO('test/idonotexist.txt')

    def test_load(self):
        file = FileIO('test/to_be.txt')
        file.load()
        assert file.data == self.test_data

    def test_save(self, tmp_path):
        out = tmp_path / 'out.txt'
        file = FileIO('test/to_be.txt', str(out))
        file.data = self.test_data
        file.save()
        with out.open('r') as check_file:
            assert check_file.read() == self.test_data

    def test_save_no_load(self):
        file = FileIO('test/to_be.txt', 'test/out.txt')
        with pytest.raises(RuntimeError):
            file.save()
