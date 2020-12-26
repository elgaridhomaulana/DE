## Spotting and fixing bugs

To find bugs in functions, you need to follow a four step procedure.

<li>
<ol>Write unit tests.</ol>
<ol>Run them.</ol>
<ol>Read the test result report and spot the bugs.</ol>
<ol>Fix the bugs.</ol>
</li>

## Running Tests

### Running all tests
cd tests <br>
pytest

### Running all tests but stop after found an error
pytest -x <br>
execution of test stop when encounter one error

### Running test on a specific file contains test
pytest data/test_preprocessing_helpers.py

### Running test on specific test class
pytest data/test_processing_helpers.py::TestRowToList <br>
will running 7 tests because there is 7 test in class TestRowToList

pytest data/test_processing_helpers.py::TestRowToList::test_on_one_tab_with_missing_value <br>
will running only 1 test

### Running test with keyword extraction
pytest -k "TestSplitIntoTrainingAndTestingSets" <br>
or <br>
pytest -k "TestSplit"

### Mocking
Ketika suatu fungsi terdapat dependensi terhadap fungsi lain. Kita ingin hanya mengetes fungsi itu saja tanpa harus mengetes fungsi yang lainnya. Kita dapat menggunakan konsep Mocking.

Package yang digunakan untuk mocking di pytest antara lain: <br>
pytest-mock dan unittest.mock

### Creating baseline for testing plot
pytest --mpl-generate-path {{ path to baseline }} -k "test_plot_for_almost_linear_data"

for testing use pytest --mpl
