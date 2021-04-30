"""
date = '27/04/2021'
modified_date = '28/04/2021'
author = 'Mahesh Naik'
description =crete text file and perform read write operation"""

"""read and write text file
using read,write function
using append function add data in text file"""

with open('simple.txt', 'w') as f:
    a = f.write('hello mahesh how are you')
    print(a)
with open('simple.txt','r') as f:
    a = f.read()

f= open('simple.txt','r')
data = f.read()
print(data)
f.close()



