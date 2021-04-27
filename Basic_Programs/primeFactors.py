"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'Prime Facterization """
try:
    number = int(input("Enter a number to find prime factors: "))
    for num in range(2, number + 1):
# Printing the factors of a given number until it is divided
        if number % num == 0:
            prime = True
            for j in range(2, (num // 2 + 1)):
                if num % j == 0:
                    prime = False
                    break
            if prime:
                print("%d" % num, end=' ')
    print("are the prime factors of number", number)

except Exception:
    print("Exception occured")