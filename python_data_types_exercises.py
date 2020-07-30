# Identify the data type of the following values:

type(99.9)
# Answer: Float

type(False)
# Answer: str(ing)

type(False)
# Answer: bool

type('0')
# Answer: str

type(True)
# Answer: bool

type('True')
# Answer: str

type([{}])
# Answer: dictionary inside a list

type({'a': []})
# Answer: dict

# What data type would best represent:
# A term or phrase typed into a search box? ## string
# If a user is logged in? bool
# A discount amount to apply to a user's shopping cart? Float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? str
# The price of a product? Float
# A Matrix? dict
# The email addresses collected from a registration form? list
# Information about applicants to Codeup's data science program? dict

# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.
'1' + 2
# type error

6 % 4
# 2

type(6 % 4)
# int

type(type(6 % 4))
# type

'3 + 4 is ' + 3 + 4
# TypeError

0 < 0
# False

'False' == False
# False

True == 'True'
# False

5 >= -5
# True

!False or False
# Nothing is returns in the REPL, which I think is because if something is False the REPL doesn't return anything onscreen.

True or "42"
# True - I don't understand this one fully yet.

!True && !False
# REPL returned a 'command not found' error

6 % 5
# 1

5 < 4 and 1 == 1
# False

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False

4 >= 0 and 1 !== '1'
# invalid syntax error


6 % 3 == 0
# True

5 % 2 != 0
# True

[1] + 2
# TypeError. Can't concatenate list, not an int to a list.

[1] + [2]
[1, 2]

[1] * 2
 [1, 1]

[1] * [2]
# TypeError

[] + [] == []
# True

{} + {}
# TypeError, unsuported operand type for dict

# Write some Python code, that is, variables and operators, to describe the following scenarios.

# 1. You have rented some movies for your kids: 
little_mermaid = (3 * 3)

brother_bear = (5 * 3)

hercules_movie = (1 * 3)

total_movie_rental = little_mermaid + brother_bear + hercules_movie
print(total_movie_rental)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook
google_pay = 400 #per hour
amazon_pay = 380 #per hour
facebook_pay = 350 #per hour

hours_worked_google = 6
hours_worked_amazon = 4
hours_worked_facebook = 10

weekly_pay = (google_pay * hours_worked_google) + (amazon_pay * hours_worked_amazon) + (facebook_pay * hours_worked_facebook)
print(weekly_pay)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_opening = True
current_student_schedule = 'open at 2pm'
class_schedule = 'open at 2pm'

if class_opening == True:
    print('Class has an opening')

if current_student_schedule == class_schedule:
    print('student can attend the class')

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

basket_size = 3
premium_membership = True
offer_expired = False

if (basket_size >= 2 and offer_expired == False) or premium_membership == True:
    print('Give discount')
else:
    print('Do not give discount')
# I don't think I built this perfectly logically, but I think it covers this exercise.
# I see a problem with the logic in the 'if' statement - what happens if the basket size is less than 2?
# Then the logic would incorrectly return False (I think), because of the and statment.

username = 'codeup'
password = 'notastrongpassword'

password_len = True
username_len = True
password_username_comp = True
whitespace_bonus = True