"""
date = '24/04/2021'
modified_date = '24/04/2021'
author = 'Mahesh Naik'
description = Stop watch problem"""
import time
import logging

from logicallog import logger


def stopwatch(sec):
    logger.setLevel(logging.INFO)
    """
    import time package
    define function for stopwatch format
        time b/w start and end clicks
        
    """
    min = (sec // 3600)//60
    sec = ((sec % 3600)%60)
    hours = min//3600
    logger.info('%02d:%02d:%02d' %(hours, min, sec))

time_start=input("Press key to start the time")
Start = time.time()

time_stop=input("Press key to Stop the time")
Stop = time.time()

# total time
Total_time = Stop - Start
stopwatch(Total_time)