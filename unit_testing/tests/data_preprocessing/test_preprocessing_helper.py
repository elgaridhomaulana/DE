from data_preprocessing.preprocessing_helpers import convert_to_int, row_to_list


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
