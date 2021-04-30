"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'Mahesh Naik'
description = 'Write a program Quadratic.py to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots.'
"""
import math
import logging

from funlog import logger


def quad(num1,num2,num3):
    logger.setLevel(logging.INFO)
    """print absolute value
    using square root function 
    give the user input for three numbers"""
    delta = num2 * num2 - 4 * num1 * num3

    logger.info(abs(delta))

    root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
    root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
    print("root 1: ", root1)
    print("root 2 : ", root2)
try:
    number1 = int(input("Enter number 1 :"))
    number2 = int(input("Enter number 2 :"))
    number3 = int(input("Enter number 3 :"))
    if number1 <= 0 or number1 >= 1000 or number2 <= 0 or number2 >= 1000 and number3 <= 0 or number3 >= 1000:
        logger.info("Enter number between o and 1000.")
    quad(number1, number2, number3)
except Exception:
    logger.exception("Please enter numbers in valid range.")