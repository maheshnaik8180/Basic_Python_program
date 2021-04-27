"""
date = '24/04/2021'
modified_date = '24/04/2021'
author = 'Mahesh Naik'
description = '  Coupon number problem'
"""

import random

while True:
    try:
        number_of_coupon = int(input("Enter how many distinct coupons want to generate :"))
        if number_of_coupon > 0:
            break
        else:
            print("Invalid input!!")
    except:
        print("Invalid input !!")

""" get input from user to genearte n random coupon numbe"""
def coupon_number(number_of_coupons):
    coupons=0
    random_numbers=0
    """check the random numbers in loop check the number is not in random nums 
        and append the number is random_nums list"""
    random_nums=[]
    while coupons!=number_of_coupon:
        number = random.randint(1, 10**4)
        if number not in random_nums:
            random_nums.append(number)
            coupons+=1

    print(random_nums)
coupon_number(number_of_coupon)
