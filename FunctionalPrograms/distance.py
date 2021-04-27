"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'Mahesh Naik'
description = 'Write a program Distance.py that takes two integer command-line arguments x and y and
                prints the Euclidean distance from the point (x, y) to the origin (0, 0). The formulae to
                calculate distance = sqrt(x*x + y*y). Use Math.power function'"""
import math


# create fuction for calculating distance
def distance(x1, y1):
    diff = math.sqrt((x1 ** 2 + y1 ** 2))
    print(diff)

try:
# taking inputs x and y
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    if x <= 0 or x >= 1000 or y <= 0 or y >= 1000:

        distance(x, y)
except Exception:
    print("Exception occured")