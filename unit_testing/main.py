import pytest
import numpy as np

from data_preprocessing.preprocessing_helpers import convert_to_int
from features.as_numpy import get_data_as_numpy_array
from models.train import split_into_training_and_testing_sets

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    assert actual == expected, message

def test_on_clean_file():
    expected = np.array(
        [
            [2081.0, 314942.0],
            [1059.0, 186606.0],
            [1148.0, 206186.0]
        ]
    )

    actual = get_data_as_numpy_array("data/example_clean_data_file.txt", num_columns=2)
    message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
    assert actual == pytest.approx(expected), message

def test_on_six_rows():
    example_argument = np.array(
        [
            [2081.0, 314942.0], [1059.0, 186606.0],
            [1148.0, 206186.0], [1506.0, 248419.0],
            [1210.0, 214114.0], [1697.0, 277794.0]
        ]
    )

    expected_training_array_num_rows = 4
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)

    assert actual[0].shape[0] == expected_training_array_num_rows, \
        "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    assert actual[1].shape[0] == expected_testing_array_num_rows, \
        "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)

# context manager pytest
with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!")

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match(expected_error_msg)