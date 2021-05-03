# Import the module
import json


class filehandling:

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





