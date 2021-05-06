"""
date = '29/04/2021'
modified_date = '30/04/2021'
author = 'Mahesh Naik'
description = '  CSV filehandling read and write data using oops concept'
"""


# Import the module
import json


class filehandling:
    """write data with open statement
        using append method add data in list
        """
    def datawrite(self):
        data = ""
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Mahesh',
        'website': 'naikmahesh.com',
        'from': 'Kolhapur'
    })
    data['people'].append({
        'name': 'sagar',
        'website': 'google.com',
        'from': 'Latur'
    })
    data['people'].append({
        'name': 'Sheetal',
        'website': 'apple.com',
        'from': 'Nashik'
    })

    with open('dataoops.json', 'w') as outfile:
        json.dump(data, outfile)


    def dataread(self):
        """
        read data from json file
        using open close file method
        @return:
        """
        print("read data from json file")
        with open('data.json') as json_file:
            data = json.load(json_file)
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')

# object instantiated
write = filehandling()
# function call to Write csv file and add data data frame
filewrite= write.datawrite()
# object instantiated
read = filehandling()
# function call to Write csv file and add data data frame
file= read.dataread()





