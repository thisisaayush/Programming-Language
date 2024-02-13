#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    encrypted_string = ""
    
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            base = ord('a') if char.islower() else ord('A')  # Determine the base ASCII value for lowercase or uppercase
            encrypted_char = chr((ord(char) - base + k) % 26 + base)  # Apply Caesar Cipher rotation
            encrypted_string += encrypted_char
        else:
            encrypted_string += char  # Keep non-letter characters unchanged
    
    return encrypted_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
