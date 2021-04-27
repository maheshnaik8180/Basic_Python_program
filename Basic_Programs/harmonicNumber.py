"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Harmonic Number '
given user input find harmonic function """


try:
#take user input from user
    number = int(input("Enter the value of nth number : "))
    s = 0.0
    for num in range(1, number + 1):
        # Every time of the loop taking the sum of the next harmonic number
        s = s + 1 / num
# Every time of the loop taking the sum of the next harmonic number
    print("Sum is: ", round(s, 3))

except Exception:
    print("Exception occurred")