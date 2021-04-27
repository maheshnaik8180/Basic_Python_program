"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Mahesh Naik'
description = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
"""
try:
    # Given user input Row size and Column Size
    row=int(input("Enter rows size: "))
    column=int(input("Enter column size: "))
    element=[]
    # For printing the array
    print("Enter the entries:")
    for i in range(row):
        a = []
        for j in range(column):
            a.append(int(input()))
        element.append(a)

    print(element)
except Exception:
    print("Exception Error ")
