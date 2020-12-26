from math import cos, pi, sin
import numpy as np
import pytest

from models.train import split_into_training_and_testing_sets, model_test, train_model


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

    def test_on_one_dimensional_array(self):
        test_argument = np.array([1382.0, 390167.0])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must be two dimensional. Got 1 dimensional array instead!"
        assert exc_info.match(expected_error_msg)


class TestTrainModel(object):
    def test_on_linear_data(self):
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected_slope = 2.0
        expected_intercept = 1.0
        actual_slope, actual_intercept = train_model(test_argument)
        slope_message = ("train_model({0}) should return slope {1}, "
                         "but it actually returned slope {2}".format(test_argument, expected_slope, actual_slope)
                         )
        intercept_message = ("train_model({0}) should return intercept {1}, "
                             "but it actually returned intercept {2}".format(test_argument,
                                                                             expected_intercept,
                                                                             actual_intercept
                                                                             )
                             )
        assert actual_slope == pytest.approx(expected_slope), slope_message
        assert actual_intercept == pytest.approx(expected_intercept), intercept_message

    def test_on_positively_correlated_data(self):
        test_argument = np.array([[1.0, 4.0], [2.0, 4.0],
                                  [3.0, 9.0], [4.0, 10.0],
                                  [5.0, 7.0], [6.0, 13.0],
                                  ]
                                 )
        actual_slope, actual_intercept = train_model(test_argument)
        assert actual_slope > 0, "Expected slope: > 0, Actual slope: {0}".format(actual_slope)


class TestModelTest(object):
    def test_on_perfect_fit(self):
        # Assign to a NumPy array containing a linear testing set
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        # Fill in with the expected value of r^2 in the case of perfect fit
        expected = 1.0
        # Fill in with the slope and intercept of the model
        actual = model_test(test_argument, slope=2, intercept=1.0)
        # Complete the assert statement
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_circular_data(self):
        theta = pi / 4.0
        test_argument = np.array(
            [
                [0.0, 1.0], [cos(theta), sin(theta)],
                [1.0, 0.0], [cos(3 * theta), sin(3 * theta)],
                [0.0, -1.0], [cos(5 * theta), sin(5 * theta)],
                [-1.0, 0.0], [cos(7 * theta), sin(7 * theta)]
            ]
        )

        actual = model_test(test_argument, slope=0.0, intercept=0.0)
        assert actual == pytest.approx(0.0)

    def test_on_one_dimensional_array(self):
        test_argument = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_argument, 1.0, 1.0)
        expected_error_msg = "Argument testing_set must be two dimensional. Got 1 dimensional array instead!"
        assert exc_info.match(expected_error_msg)
