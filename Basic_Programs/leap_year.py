"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Leap Year check the year is
leap year or not given user input'
"""

year=int(input("Enter a year: "))
minyear=1000
maxyear=9999

"""check the user input minimum and maximum limit"""
if year >= minyear and year <= maxyear :
        if year % 4 == 0 and year % 100 != 0:
            # checking the condition if the given year is leap year or not
            print ("Entered year is a Leap Year ")
        elif year % 400 == 0:
            print("Entered year is a Leap Year ")
        else:
            print ("Entered year is not a Leap Year ")
else:
    print ("Invalid Year, Please Enter 4 digit valid year ")