

# ### Function Exercises
# 
# - Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function


# Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if type(x) == str or type(x) == int or type(x) == float:
        return True
    else:
        return False
    
assert is_two(2) == True
assert is_two("2") == True
assert is_two(2.0) == True
assert is_two(True) == False
print("Exercise is correct")




# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(value):
    vowels = ["a", "e", "i", "o", "u"]
    assert type(value) == str, "Input must be a string"
    if value.lower() in vowels:
        return True
    else:
        return False

assert is_vowel("A") == True
assert is_vowel("V") == False
print("Exercise is correct")



# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(value):
    are_vowels = ["a", "e", "i", "o", "u"]
    assert type(value) == str, "Input must be a string"
    if value.lower() not in are_vowels:
        return True
    else:
        return False
    
assert is_consonant("A") == False
assert is_consonant("V") == True
print("Exercise is correct")



# Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.


# My breakdown of the logic of the problem:
    # does value start with a consonant? [step 1]
        # Have to figure out the 'not in' of a list of vowels...
    # if so, then capitalize it
    # if not, then return 'value'
    # For example, this function would capitalize the string "Banana", while the string "apple" it would not.

def string_word(value):
    vowel_list = ["a", "e", "i", "o", "u"]
    if value[0] not in vowel_list:
        return value.capitalize()
    else:
        return value

assert string_word("apple") == "apple"
assert string_word("banana") == "Banana"
print("Exercise is correct") 



# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill, tips): # Added two parameters to function definition, since problem asked for two entries
    assert type(bill) == float, "Please use a float"  # Assertions to make sure float is used...
    assert type(tips) == float, "Please use a float"
    amt_to_tip = bill * tips   # Created new variable (within function) that did the math required to find the tip
    return amt_to_tip          # End of function; should return the specific tip amount 
    
assert calculate_tip(25.0, .2) == 5.0 # assert tests
assert calculate_tip(30.0, .1) == 3.0
print("Exercise is correct") # Copied this idea from the 101 exercises, so I had a visual output to make sure the function worked.


# Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, discount):
    assert type(price) == int
    assert type(discount) == float
    discount_amt = price * discount
    discount_applied = price - discount_amt
    return discount_applied

assert apply_discount(25, .2) == 20
assert apply_discount(10, .1) == 9
print("Exercise is correct")





# Define a function named handle_commas. It should accept a string that is a number that contains
# commas in it as input, and return a number as output.

def handle_commas(c):
    remove_commas = c.replace(",","")
    return float(remove_commas)

print(handle_commas("1,000"))
    
assert handle_commas("1,000") == 1000
assert handle_commas("2,000") == 2000
print("Exercise is correct")


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    #  x = int(x) found it interesting that adding this would allow me to use "80" as the function input and it would successfully complete the function.
    assert type(x) == int, "Please use an integer, not a float or letters"

    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    elif x < 60:
        return "F"
    else:
        return "Please use integers, not a float or a letters"


assert get_letter_grade(85) == "B"
assert get_letter_grade(99) == "A"
print("Exercise is correct")




# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# Logic/breakdown of problem:
    # intake string (make sure it is)
    # convert to list (so I can iterate)
    # iterate through checking for vowels
    # create new list purged of vowels (for n in n NOT IN 'aeiou'? --> then return the new list?)
    # finally, on the return line (or line above, needing extra code), convert back to string

def remove_vowels(c):
    assert type(c) == str, "Please only enter a string."
    no_vowel = c.lower()
    vowels = ("a", "e", "i", "o", "u") # I realize this is a tuple, but I tested this using a list as got the same result. Figured using a tuple was (maybe) a bit safer since it's immutable.
    for x in c.lower(): # This extra .lower() may not be needed now.
        if x in vowels:
            no_vowel = no_vowel.replace(x, "")
    return no_vowel

assert remove_vowels("banana") == "bnn"
assert remove_vowels("Apple") == "ppl"
assert remove_vowels("CodeUp") == "cdp"
print("Exercise is correct")





# Define a function named normalize_name. It should accept a string and return a valid python identifier, 
# that is:
#     anything that is not a valid python identifier should be removed
#     leading and trailing whitespace should be removed
#     everything should be lowercase
#     spaces should be replaced with underscores
#     for example:
#         Name will become name
#         First Name will become first_name
#         % Completed will become completed

def normalize_name(x):
    valid_string = x.lstrip("0123456789 ")
    valid_string = valid_string.lower()
    valid_string = valid_string.replace(" ","_")

    valid_strings = ""

    for n in valid_string:
        if n not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
            valid_strings += n
    if valid_strings.isidentifier() == False:
        print("this didn't trigger")
        return "Error at isidentifier"
    return valid_strings

assert normalize_name("Hello!") == "hello"
assert normalize_name("First Name") == "first_name"
print("Exercise is correct")



# Define a function named normalize_name. It should accept a string and return a valid python identifier, 
# that is:
#     anything that is not a valid python identifier should be removed
#     leading and trailing whitespace should be removed
#     everything should be lowercase
#     spaces should be replaced with underscores
#     for example:
#         Name will become name
#         First Name will become first_name
#         % Completed will become completed

def normalize_name(x):
    valid_string = x.lstrip("0123456789 ")
    valid_string = valid_string.lower()
    valid_string = valid_string.replace(" ","_")

    valid_strings = ""
    for n in valid_string:
        if n not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
            valid_strings += n        
    final_string = ""
    for c in valid_strings:
        if valid_strings.isidentifier():
            final_string += c
    return final_string

assert normalize_name("Hello!") == "hello"
assert normalize_name("First Name") == "first_name"
print("Exercise is correct")





# Write a function named cumulative_sum that accepts a list of numbers and returns a
# list that is the cumulative sum of the numbers in the list.

def cumulative_sum(x):
    assert type(x) == list
    cumulative_num = [sum(x[:i + 1]) for i in range(len(x))]
    return cumulative_num

assert normalize_name("Hello!") == "hello"
assert normalize_name("First Name") == "first_name"
print("Exercise is correct")


# ### Bonus Questions
# - 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.



# Two ways I'm thinking I can do this:
# 1. I can import the datetime module. Figure it out that way
# 2. Or, I can do it backwards; figure out what the function that converts from military time to 12 hours works
# and then that'll be the reverse for the main bonus question.

# Steps:
    # Isolate the "am" and "pm". check
    # create a variable or list(?) that allocates the time based on if it's am/pm. Use > and <??
    # do an if/elif statement that converts the time based on am/pm.
    # Return the military time once converted.




import datetime

def twelveto24(time = datetime.datetime.now().time().strftime("%I:%M%p")):
    assert type(time) == str, "Please enter a string in this format: 'HH:MMPM'"
    assert time[2] == ":", "Please enter a string in this format: 'HH:MMPM'"
    if time[-2:].lower() == "am":
        morning_check = time[:2]
        morning_check += ":" + time[3:5]
        final_time = morning_check
    else:
        afternoon_check = int(time[:2])
        afternoon_check = str(afternoon_check + 12)
        afternoon_check += ":" + time[3:5]
        final_time = afternoon_check
    return final_time

assert twelveto24("08:24AM") == "08:24"
assert twelveto24("10:12PM") == "22:12"
print("Exercise is correct")


print("Running the function for testing")

twelveto24()




# Bonus write a function that does the opposite.

import datetime

def twentyfourto12(time = datetime.datetime.now().time().strftime("%H:%M")):
    assert type(time) == str, "Please enter a string in this format: 'HH:MM'"
    assert time[2] == ":", "Please enter a string in this format: 'HH:MM'"
    if int(time[:2]) < 12:
        morning_twelve_check = time + " AM"
        final_time = morning_twelve_check
    else:
        afternoon_twelve_check = int(time[:2])
        afternoon_twelve_check = str(afternoon_twelve_check - 12)
        afternoon_twelve_check += ":" + time[3:5] + " PM"
        final_time = afternoon_twelve_check
    return final_time
    

print("Running the function for testing")
twentyfourto12("13:45")


# - Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#     - col_index('A') returns 1
#     - col_index('B') returns 2
#     - col_index('AA') returns 27


