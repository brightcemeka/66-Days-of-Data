file_to_open = open('greeting.txt', 'r') #w, a
print(file_to_open.read())
print(file_to_open.readline())
print(file_to_open.readline())

line_by_line = file_to_open.readlines()
line_by_line1 = file_to_open.read().splitlines()

#close the file
file_to_open.close()

#Hackerrank Questions
import math
import os
import random
import re
import sys

# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and (n >= 2 and n <= 5):
        print("Not Weird")
    elif n % 2 == 0 and (n >= 6 and n <= 20):
        print("Weird")
    elif n % 2 == 0 and (n > 20):
        print("Not Weird")
