"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Prime Facterization '
"""
import logging

from basiclogger import logger

logger.setLevel(logging.INFO)
try:
    """given User Input Printing the factors of a given number until it is divided
    check the numbers in given condition in loop I,J,K
    print the prime factor number"""
    number = int(input("Enter a number to find prime factors: "))
    for num in range(2, number + 1):
        if number % num == 0:
            prime = True
            for j in range(2, (num // 2 + 1)):
                if num % j == 0:
                    prime = False
                    break
            if prime:
                print("%d" % num, end=' ')
    logger.info("are the prime factors of number")
    logger.info( number)

except Exception:
    logger.exception("Exception occured")