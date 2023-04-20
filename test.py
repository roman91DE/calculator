#!/usr/bin/env python3

from subprocess import run

# write a python script that tests the calc.py script
# write some arithmetic expressions that contain the following operators: +, -, *, /, ^ and their results
# the tested script should return the correct results for each expression

# create a dictionary with the test cases and their results
# the keys should be the test cases and the values should be the results
# include test cases that lead to decimal results
# the test cases should be strings
# the results should be floats
CASES = {
    "1 + 1": 2.0,
    "2 - 1": 1.0,
    "2 * 2": 4.0,
    "4 / 2": 2.0,
    "2 ^ 2": 4.0,
    "1 + 1 + 1": 3.0,
    "2 - 1 - 1": 0.0,
    "2 * 2 * 2": 8.0,
    "4 / 2 / 2": 1.0,
    "2 ^ 2 ^ 2": 16.0,
    "1 + 1 * 2": 3.0,
    "2 - 1 * 2": 0.0,
    "2 * 2 + 2": 6.0,
    "4 / 2 + 2": 4.0,
    "2 ^ 2 + 2": 6.0,
    "1 + 1 * 2 ^ 2": 5.0,
    "2 - 1 * 2 ^ 2": -2.0,
    "2 * 2 + 2 ^ 2": 10.0,
    "4 / 2 + 2 ^ 2": 6.0,
    "2 ^ 2 + 2 * 2": 10.0,
    "1 + 1 * 2 ^ 2 - 2": 3.0,
    "2 - 1 * 2 ^ 2 + 2": 2.0,
    "2 * 2 + 2 ^ 2 / 2": 5.0,
    "4 / 2 + 2 ^ 2 * 2": 12.0,
    "2 ^ 2 + 2 * 2 - 2": 8.0,
    "1 + 1 * 2 ^ 2 - 2 / 2": 3.0,
    "2 - 1 * 2 ^ 2 + 2 / 2": 2.0,
    "2 * 2 + 2 ^ 2 / 2 * 2": 10.0,
    "4 / 2 + 2 ^ 2 * 2 / 2": 6.0,
    "2 ^ 2 + 2 * 2 - 2 / 2": 8.0,
    "1 + 1 * 2 ^ 2 - 2 / 2 + 2": 5.0,
    "2 - 1 * 2 ^ 2 + 2 / 2 - 2": 0.0,
    "2 * 2 + 2 ^ 2 / 2 * 2 + 2": 12.0,

}


# write all 10 test cases in  loop
# use the CASE1, CASE2, ... variables as input
# use the RESULT1, RESULT2, ... variables as expected output
# use the print() function to print the test case number and the result of the test case
# use the if statement to check if the result of the test case is correct

for case, result in CASES.items():
    output = run(["python", "/Users/rmn/Repos/calculator/calc.py", case], capture_output=True, text=True).stdout.strip()
    if float(output) == float(result):
        print("Test case " + case + " passed")
    else:
        print("Test case " + case + " failed")
        print(f"Output: {output}, Result: {result}")
    #print(f"Output: {output}, Result: {result}")
