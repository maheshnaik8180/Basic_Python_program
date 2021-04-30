"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Leap Year'
Check if leap year or not"""

import logging

from basiclogger import logger
logger.setLevel(logging.INFO)
year=int(input("Enter a year: "))
minyear=1000
maxyear=9999

"""check the user input minimum and maximum limit
    check year is leap year or not using conditional statement  """
if year >= minyear and year <= maxyear :
        if year % 4 == 0 and year % 100 != 0:
            logger.info ("Entered year is a Leap Year ")
        elif year % 400 == 0:
            logger.info("Entered year is a Leap Year ")
        else:
            logger.info ("Entered year is not a Leap Year ")
else:
    logger.info ("Invalid Year, Please Enter 4 digit valid year ")