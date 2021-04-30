"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'Mahesh Naik'
description = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
given user input replace the word
using length function calculate length"""
import logging

from basiclogger import logger

logger.setLevel(logging.INFO)
try:
    username = str(input("Enter Name: "))
    length = len(username)
    if length >= 3:
       logger.info(f"hello {username}, How are you?")
    else:
        logger.info("username should be minimum 3 character")

except Exception:
        logger.exception("Exception occured")
