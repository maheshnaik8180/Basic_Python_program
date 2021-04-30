"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Mahesh Naik'
description = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
"""
import logging

from funlog import logger

logger.setLevel(logging.INFO)

try:

    """Given user input Row size and Column Size
    using append function add element in array
         For printing the array
    """
    row=int(input("Enter rows size: "))
    column=int(input("Enter column size: "))
    element=[]

    print("Enter the entries:")
    for i in range(row):
        a = []
        for j in range(column):
            a.append(int(input()))
        element.append(a)

    logger.info(element)
except Exception:
    logger.exception("Exception Error ")
