#!/usr/bin/python3
import sys
from math import isqrt

def factorize(num):
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return f'{num}={num // i}*{i}'

if len(sys.argv) != 2:
    print('Usage: factors <filename>')
    sys.exit(1)

file_input = sys.argv[1]

with open(file_input, 'r') as file:
    if not  file:
        print(f"Error: can't open file {sys.argc[1]}")

    for value in file:
        number = int(value)
        print(factorize(number))