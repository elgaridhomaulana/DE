from unittest.mock import call
import pytest
from data_preprocessing.preprocessing_helpers import (
    convert_to_int, row_to_list, preprocess
)


@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_path = tmpdir.join("raw.txt")
    clean_path = tmpdir.join("clean.txt")
    with open(raw_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    return raw_path, clean_path


def row_to_list_bug_free(row):
    return_values = {"1,801\t201,411\n": ["1,801", "201,411"],
                     "1,767565,112\n": None,
                     "2,002\t333,209\n": ["2,002", "333,209"],
                     "1990\t782,911\n": ["1990", "782,911"],
                     "1,285\t389129\n": ["1,285", "389129"],
                     }
    return return_values[row]


def convert_to_int_bug_free(comma_separated_integer_string):
    return_values = {"1,801": 1801,
                     "201,411": 201411,
                     "2,002": 2002,
                     "333,209": 333209,
                     "1990": None,
                     "782,911": 782911,
                     "1,285": 1285,
                     "389129": None,
                     }
    return return_values[comma_separated_integer_string]


class TestConvertToInt(object):

    def test_on_string_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
        assert actual == expected, message


class TestRowToList(object):
    # TESTING WELL: Boundary values
    def test_on_no_tab_no_missing_value(self):  # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_two_tabs_no_missing_value(self):  # (2, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, f"Expected: None, Actual: {actual}"

    def test_on_one_tab_with_missing_value(self):    # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    # TESTING WELL: Values triggering special logic
    def test_on_no_tab_with_missing_value(self):    # (0, 1) case
        # Assign to the actual return value for the argument "\n"
        actual = row_to_list('\n')
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_with_missing_value(self):    # (2, 1) case
        # Assign to the actual return value for the argument "123\t\t89\n"
        actual = row_to_list("123\t\t89\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    # TESTING WELL: Normal arguments
    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        # Fill in with the expected return value for the argument "123\t4,567\n"
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        # Write the assert statement along with a failure message
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


class TestPreprocess(object):
    def test_on_raw_data(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        row_to_list_mock = mocker.patch(
            "data_preprocessing.preprocessing_helpers.row_to_list",
            side_effect=row_to_list_bug_free
        )
        convert_to_int_mock = mocker.patch(
            "data_preprocessing.preprocessing_helpers.convert_to_int",
            side_effect=convert_to_int_bug_free
        )
        preprocess(raw_path, clean_path)
        assert row_to_list_mock.call_args_list == [
            call("1,801\t201,411\n"), call("1,767565,112\n"),
            call("2,002\t333,209\n"), call("1990\t782,911\n"),
            call("1,285\t389129\n")
        ]
        assert convert_to_int_mock.call_args_list == [
            call("1,801"), call("201,411"), call("2,002"),
            call("333,209"), call("1990"),  call("782,911"),
            call("1,285"), call("389129")
        ]

        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1801\t201411\n"
        second_line = lines[1]
        assert second_line == "2002\t333209\n"
