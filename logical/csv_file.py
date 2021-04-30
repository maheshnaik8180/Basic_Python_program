"""
date = '27/04/2021'
modified_date = '28/04/2021'
author = 'Mahesh Naik'
description =crete CSV file and perform read write operation"""

"""read and write CSV file
using read,write function
using append function add data in CSV file"""
import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

#read the csv file
f=open('names.csv')
csv = csv.reader(f)
for row in csv:
 print(row)
