"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'Mahesh Naik'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
"""
import math
import logging

from funlog import logger

logger.setLevel(logging.INFO)
try:
    """input temperature
    input wind speed
    param:temp= temperature
    temperature value is greater than 0 to less than 50  
    speed value is greater than 3 and less than 120
    calculate windchill formula"""
    temp=int(input("Temperature is: "))
    if temp>=0 and temp<=50:
      # input wind speed
     speed = int(input("Wind speed is: "))
     if speed > 3 and speed < 120:

      """ calculate windchill formula"""
      wind = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * (math.pow(speed, 0.16))
     logger.info("Wind chill is: ", wind)
    else:
     logger.info("Enter correct values!")

except Exception:
    logger.exception("Exception Error")

