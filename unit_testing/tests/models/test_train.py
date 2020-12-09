from models.train import split_into_training_and_testing_sets
import numpy as np
import pytest

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)
    
    def test_on_six_rows(self):
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
    
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        # Store information about raised ValueError in exc_info
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        # Check if the raised ValueError contains the correct message
        assert exc_info.match(expected_error_msg)