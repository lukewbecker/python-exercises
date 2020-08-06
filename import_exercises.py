# Import Exercises

# Libraries and files needed to run this code:
#   time
#   os
#   datetime
#   itertools
#   re (regex)
#   importing a local file, profiles.json per instructions

# Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:


# import the module and refer to the function with the . syntax

import time

time.ctime()


# Use from to import the function directly
from datetime import datetime, timedelta

datetime.datetime.now().time().strftime("%I:%M %p")

# Use from and give the function a different name
import os as operating_system

operating_system

# Running another imported function from the datetime module:
datetime.datetime.now()


# For the following exercises, read about and use the itertools module 
# from the standard library to help you solve the problem.

import itertools

letter_count = list(itertools.product('abc', '123'))
len(letter_count)
print(f"You can combine 'abc' and '123' in {len(letter_count)} different ways")
print(letter_count)

# How many different ways can you combine two of the letters from "abcd"?


    # Use this function to get only unique combinations, in a list
lettering_count = list(itertools.combinations("abcd", 2))   

    # Count how many entries are in the list
len(lettering_count)

    # print out formatted answer to include the result of the count of elements in the list I created.
print(f"You can combine 'abcd' in {len(lettering_count)} different ways")
print(lettering_count)  


# Using this data, write some code that calculates and outputs the following information:
    # Total number of users
    # Number of active users
    # Number of inactive users
    # Grand total of balances for all users
    # Average balance per user
    # User with the lowest balance
    # User with the highest balance
    # Most common favorite fruit
    # Least most common favorite fruit
    # Total number of unread messages for all users

import json
jsonprofile_load = open('profiles.json')
jpd = json.load(jsonprofile_load)

# Total number of users

total_users_count = len(key_id)
print(f"Total number of users is: {total_users_count}")


# Number of active users
def check_active():
    check_a = [x["_id"] for x in jpd if x["isActive"] == True]
    return len(check_a)
    
check_active()

# Number of inactive users

def not_active():
    check_na = [x["_id"] for x in jpd if x["isActive"] == False]
    return len(check_na)
not_active()


# Grand total of balances for all users

def grand_total():
    total_balance = 0
    for x in jpd:
        total_balance += float(x["balance"].replace(",","").replace("$",""))
    return total_balance
grand_total()


# Average balance per user

def avg_bal():
    total_balance = grand_total
    user_num = len(key_id)
    user_avg_bal = (grand_total() / user_num)
    return user_avg_bal
avg_bal()




# User with the lowest balance

def user_min_bal():
    minimum_bal = min([x["balance"] for x in jpd])
    user_name = [n["name"] for n in jpd if n["balance"] == minimum_bal]
    return user_name
user_min_bal()

# User with the highest balance

def user_max_bal():
    max_bal = max([x["balance"] for x in jpd])
    user_name = [n["name"] for n in jpd if n["balance"] == max_bal]
    return user_name
user_max_bal()

# Most common favorite fruit


def favorite_fruit():
    a = 0
    b = 0
    s = 0
    for x in jpd:
        if x["favoriteFruit"] == "apple":
            a += 1
        elif x["favoriteFruit"] == "banana":
            b += 1
        elif x["favoriteFruit"] == "strawberry":
            s += 1
#         print(a, x["favoriteFruit"])
#         print(b, x["favoriteFruit"])
#         print(s, x["favoriteFruit"])
    fruit_total = [{"fruit": "apple", "num": a}, {"fruit": "banana", "num": b}, {"fruit": "strawberry", "num": s}]
    # creating a tuple:
    max_fruit = (max([x["num"] for x in fruit_total]), max([x["fruit"] for x in fruit_total]))
    return max_fruit
favorite_fruit()

# Least most common favorite fruit

def least_favorite_fruit():
    a = 0
    b = 0
    s = 0
    for x in jpd:
        if x["favoriteFruit"] == "apple":
            a += 1
        elif x["favoriteFruit"] == "banana":
            b += 1
        elif x["favoriteFruit"] == "strawberry":
            s += 1
#         print(a, x["favoriteFruit"])
#         print(b, x["favoriteFruit"])
#         print(s, x["favoriteFruit"])
    fruit_total = [{"fruit": "apple", "num": a}, {"fruit": "banana", "num": b}, {"fruit": "strawberry", "num": s}]
    # creating a tuple:
    min_fruit = (min([x["num"] for x in fruit_total]), min([x["fruit"] for x in fruit_total]))
    return min_fruit

least_favorite_fruit()


# Total number of unread messages for all users
# Going to test using Regex module. I'm not sure I like what all that modeule does, but I think it's good to try something new and learn.

import re

def total_msgs():
    total_unread = 0
    # convert all greetings to one big string
    string_convert = str([x['greeting'] for x in jpd])
    # Extract all numbers, as a list of strings
    msg_nums = re.findall('[0-9]+', string_convert)
    # Convert strings to ints, using list comprehension
    msg_nums = [int(i) for i in total_msg_count_2]
    # Now, sum the list for total unread msgs
    total_unread = sum(msg_nums)
    return total_unread
total_msgs()
print(f"The total number of unread messages is: {total_msgs()}.")

# I'm sure there's a much more elegant way to accomplish this problem. I'm looking forward to seeing how others solved it.

