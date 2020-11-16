## Spotting and fixing bugs

To find bugs in functions, you need to follow a four step procedure.

<li>
<ol>Write unit tests.</ol>
<ol>Run them.</ol>
<ol>Read the test result report and spot the bugs.</ol>
<ol>Fix the bugs.</ol>
</li>

In a previous exercise, you wrote a unit test for the function convert_to_int(), which is supposed to convert a comma separated integer string like "2,081" to the integer 2081. You also ran the unit test and discovered that it is failing.

In this exercise, you will read the test result report from that exercise in detail, and then spot and fix the bug. This would equip you with all basic skills to start using unit tests for your projects.

The convert_to_int() function is defined in the file preprocessing_helpers.py. The unit test is available in the test module test_convert_to_int.py.