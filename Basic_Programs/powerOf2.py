"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Power of 2 Given user Input print the power of 2 '
"""
import logging

from basiclogger import logger

logger.setLevel(logging.INFO)
"""check power of number using power function 
    use for loop check the condition and 
    print the number of power"""
try:
    power = int(input("enter number :"))

    def powerOfTwo(power):

        for i in range(power + 1):
            logger.info(f"2^{i}={2 ** i}")

        logger.info("print valid data type")

    powerOfTwo(power)
except Exception:
    logger.exception("exception occured")
