"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""

def addDigits(number):
    return 1 + (number - 1)  % 9 if number else 0

test_cases = [223, 123, 12, 20, 123568, 10, 1, 0]
for test in test_cases:
    print(addDigits(test))