"""
date = '24/04/2021'
modified_date = '24/04/2021'
author = 'Mahesh Naik'
description = Stop watch problem"""
import time

"""define function for stopwatch format"""
def stopwatch(sec):
    min = (sec // 3600)//60
    sec = ((sec % 3600)%60)
    hours = min//3600
    print('%02d:%02d:%02d' %(hours, min, sec))

time_start=input("Press key to start the time")
Start = time.time()

time_stop=input("Press key to Stop the time")
Stop = time.time()

# total time
Total_time = Stop - Start
stopwatch(Total_time)