#Sum_of_Three_Integers
terms=int(input("Enter how many terms you want to input: "))
numbers=[]

for i in range(terms):
    number=int(input("Enter number: "))
    numbers.append(number)
"""function to find different triplets  """
def sumOfIntergerZero(numbers,terms):
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