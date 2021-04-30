"""
date = '27/04/2021'
modified_date = '30/04/2021'
author = 'Mahesh Naik'
description =crete JSON file and perform read & write operation"""

"""read and write JSON file
    using read,write and append function
    using append function add data in JSON file"""

import json
import logging
from logicallog import logger
logger.setLevel(logging.INFO)

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

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        logger.info('Name: ' + p['name'])
        logger.info('Website: ' + p['website'])
        logger.info('From: ' + p['from'])
        logger.info('')