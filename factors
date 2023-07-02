#!/usr/bin/python3
"""Representing RSA factoring"""

import sys
from math import isqrt


def factorize(num):
    """Define factorize to factor a number

    Args:
        num (int) : integer value to be factorized

    :return:
        factorized value
    """
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return f'{num}={num // i}*{i}'


if len(sys.argv) != 2:
    print('Usage: factors <filename>')
    sys.exit(1)

file_input = sys.argv[1]

try:
    with open(file_input, 'r') as file:
        if file is None:
            print("Error: cant open file {}".format(sys.argv[1]))

        for value in file:
            number = int(value)
            print(factorize(number))
except FileNotFoundError:
    print("{} was not found".format(sys.argv[1]))

