from features.as_numpy import get_data_as_numpy_array
import numpy as np
import pytest
import os


# pytest fixture dapat digunakan untuk proses setup dan teardown
@pytest.fixture
def clean_data_file():
    # setup file_path
    file_path = "clean_data_file.txt"
    # menuliskan nilai ke dalam file txt dengan context manager
    with open(file_path, "w") as f:
        f.write("2081.0\t314942.0\n1059.0\t186606.0\n1148.0\t206186.0\n")
    yield file_path
    # menghapus apabila sudah selesai digunakan
    os.remove(file_path)


@pytest.fixture
def empty_file(tmpdir):
    file_path = tmpdir.join("empty.txt")
    open(file_path, "w").close()
    yield file_path


# pytest mark.usefixtures digunakan untuk menggunakan fixture dalam class
@pytest.mark.usefixtures("clean_data_file", "empty_file")
class TestGetDataAsNumpyArray(object):

    def test_on_clean_file(self, clean_data_file):
        expected = np.array(
            [
                [2081.0, 314942.0],
                [1059.0, 186606.0],
                [1148.0, 206186.0]
            ]
        )

        actual = get_data_as_numpy_array(clean_data_file, num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message

    def test_on_empty_file(self, empty_file):
        expected = np.empty((0, 2))
        actual = get_data_as_numpy_array(empty_file, 2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
