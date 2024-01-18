#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Parse the input string
    hour, minute, second = map(int, s[:-2].split(':'))
    period = s[-2:]

    # Convert to 24-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    # Format the result
    result = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return result

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
