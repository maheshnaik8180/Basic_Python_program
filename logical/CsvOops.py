"""
date = '29/04/2021'
modified_date = '30/04/2021'
author = 'Mahesh Naik'
description = '  CSV filehandling read and write data using oops concept'
"""

import pandas
import pandas as pd


class fileHandling:
        """
            reads csv file and converts contents into data frome
            :return: returns fieldname
            """
        def CSVwrite(self):

            fieldnames = pd.DataFrame([['Mahesh','Naik'], ['vikas', 'Naik'], ['rakesh', 'desai']],
                        columns=['  first_name','  last_name'])
            fieldnames.to_csv('names.csv', index=False)
            return fieldnames


        def CSVread(self):
            """
            read file using pandas function 
            @return:datafile
            """
            dataFile = pandas.read_csv('names.csv')
            print(dataFile)
            return dataFile

 # object instantiated
csv_read = fileHandling()

# function call to read csv file and Display Data
read = csv_read.CSVread()

# object instantiated
csv_write = fileHandling()
# function call to Write csv file and add data data frame
write = csv_write.CSVwrite()


