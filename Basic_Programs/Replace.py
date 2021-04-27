"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
given user input replace the word
using length function calculate length"""

try:
    username = str(input("Enter Name: "))
    length = len(username)
    if length >= 3:
       print(f"hello {username}, How are you?")
    else:
        print("username should be minimum 3 character")

except Exception:
        print("Exception occured")
