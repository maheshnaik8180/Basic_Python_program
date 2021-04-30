"""
date = '24/04/2021'
modified_date = '24/04/2021'
author = 'Mahesh Naik'
description = '  Coupon number problem'
"""

import random
import logging

from logicallog import logger

"""
    :param number: no of coupons wants to print
    :return:
    get user input and check how many coupons want to generate
    using conditional statement check the coupons are greate than 0 or not
    """
while True:
    try:
        number_of_coupon = int(input("Enter how many distinct coupons want to generate :"))
        if number_of_coupon > 0:
            break
        else:
            logger.info("Invalid input!!")
    except:
        logger.info("Invalid input !!")

def coupon_number(number_of_coupons):
    logger.setLevel(logging.INFO)

    """ get input from user to genearte n random coupon numbe
        check the random numbers in loop check the number is not in random nums 
    and append the number is random_nums list
             """
    coupons=0
    random_numbers=0
    random_nums=[]
    while coupons!=number_of_coupon:
        number = random.randint(1, 10**4)
        if number not in random_nums:
            random_nums.append(number)
            coupons+=1

    logger.info(random_nums)
coupon_number(number_of_coupon)
