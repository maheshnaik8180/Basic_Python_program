"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Mahesh Naik'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
"""
#Sum_of_Three_Integers
terms=int(input("Enter how many terms you want to input: "))
numbers=[]

for i in range(terms):
    number=int(input("Enter number: "))
    numbers.append(number)
"""function to find different triplets  """
def sumOfIntergerZero(numbers,terms):
 #given three numbers Add in loop And calculate
    count=0
    for i in range(terms-2):
        for j in range(terms-1):
            for k in range(terms):
                if numbers[i]+numbers[j]+numbers[k]==0:
                    count+=1
                    print(f"Triplet is ({numbers[i]},{numbers[j]},{numbers[k]})")
    return count
count=sumOfIntergerZero(numbers,terms)
print(f"Total numbers of triplets are: {count}")

""" no triplet with 0 sum found in array"""
if count==0:
    print("No triplet found")