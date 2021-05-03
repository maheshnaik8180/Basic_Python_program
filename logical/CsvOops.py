import pandas
import pandas as pd


class fileHandling:

        def CSVwrite(self):

            fieldnames = pd.DataFrame([['Mahesh','Naik'], ['vikas', 'Naik'], ['rakesh', 'desai']],
                        columns=['  first_name','  last_name'])
            fieldnames.to_csv('names.csv', index=False)
            return fieldnames


        def CSVread(self):
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



# csvPath = 'C:/Users/GENIUS/PycharmProjects/logical/names.csv'
# # object instantiated
# read = fileHandling(csvPath)
# # function call to read csv file and convert into data frame
# file = read.CSVreader()
