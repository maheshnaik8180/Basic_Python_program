
import time
"""define function for stopwatch format"""
def stopwatch(sec):
    min = sec // 60
    sec = sec % 60
    hours = min % 60
    print("Time = {0}:{1}:{2}".format(int(hours),int(min),sec))

time_start=input("Press key to start the time")
Start = time.time()

time_stop=input("Press key to Stop the time")
Stop = time.time()

# total time
Total_time = Stop - Start
stopwatch(Total_time)