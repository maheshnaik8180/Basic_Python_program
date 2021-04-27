"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Power of 2 '
"""
try:
    power = int(input("enter number :"))

    def powerOfTwo(power):
        for i in range(power + 1):
            # Printing the table of two powers
            print(f"2^{i}={2 ** i}")

        print("print valid data type")

    powerOfTwo(power)
except Exception:
    print("exception occured")
