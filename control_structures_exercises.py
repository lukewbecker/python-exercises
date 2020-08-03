# Control Structures
# - For loops
# - While loops
# - Break and Continue


# Conditional Basics


# Prompt the user for a day of the week, print out whether the day is Monday or not
day_input = input("What day of the week is it? ")

if day_input == "Monday":
    print("Today is Monday")
else:
    print("It isn't Monday")


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

day_week_input = input("What day of the week is it? ").capitalize()

if day_week_input in week_days:
    print("It is a weekday, I get to learn python!")
else:
    print("Yay it's the weekend!!!")



# Write the python code that calculates the weekly paycheck.
number_hours_worked = int(input("How many hours did you work this week? "))
my_hourly_rate = 25

if number_hours_worked > 40:
    my_hourly_rate = my_hourly_rate * 1.5
else:
    my_hourly_rate

weekly_paycheck = number_hours_worked * my_hourly_rate
print("Your hourly rate is: ")
print(my_hourly_rate)
print("And your weekly paycheck is: ")
print(weekly_paycheck)


# Loop basics question 1:
i = 5
while i <= 15:
    print(i)
    i += 1


# More basic loop exercises
n = 2
while n <= 100:
    print(n)
    n += 2


n = 100
while n >= -10:
    print(n)
    n -= 5



n = 2
while n <= 1000000:
    print(n)
    n **= 2


n = 100
while n >= 5:
    print(n)
    n -= 5



# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.
# Solution to first For loop exercise:

x = int(input("Pick a number: "))
multiples_table = list(range(1, 11))

my_list = []

for i in multiples_table:
#    print(i)
#    print(x)
    my_list.append(i * x)
    
print(my_list)


# Create a for loop that uses print to create the output shown below.

for n in range(1, 10):
    print(f"{n}" * n)


# Break and Continue Exercises

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers 
# between 1 and 50, except for the number the user entered.

user_input = 0

while user_input % 2 == 0:
    print("Please pick an odd number between 1 - 50: ")
    user_input = input("Enter an odd number: ")
    if user_input.isdigit() == False:
        user_input = 0
        continue
    else:
        user_input = int(user_input)
        if user_input % 2 != 0 and user_input > 0 and user_input < 51:
            break

for n in range(51):
    if n % 2 == 0:
        continue
    if n == user_input:
        print("Yikes! skipping number: {}".format(n))
        continue
    print('Here is an odd number: {}'.format(n))


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this 
# to a numeric type.)

number_choice = int(input("Please enter a positive number: "))

start_num = 0

while start_num <= number_choice:
    if number_choice == 0:
        number_choice = int(input("Please enter a positive number: "))
    print(start_num)
    start_num += 1



# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

number_choice = int(input("Please enter a positive number: "))

start_num = 0

while start_num <= number_choice:
    if number_choice > 0:
        print(start_num)
        start_num += 1


u_input = int(input("Pick a positive integer: "))

while u_input >= 1:
    print(u_input)
    u_input -= 1


# Fizzbuzz Questions

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.

n = 1

while n in range(1, 101):
    print(n)
    n += 1

# For multiples of three print "Fizz" instead of the number

for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    else:
        print(n)

# For the multiples of five print "Buzz".

for n in range(1, 101):
    if n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        print(n)


# All together: (extra)
for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

user_continue = "y" # initializing the code.

while user_continue != "n":
    user_number = int(input("What number would you like to go up to? "))
    print("Here is your table!")
    print("Number | Squared | Cubed")
    for number in range(1, user_number+1):
        squared = number ** 2
        cubed = number ** 3
        print(f"{number}      |   {squared}    | {cubed}")
    
    user_continue = input("Do you want to continue? y/n   ")
    
# Big thank you to Ryan for his help!!



# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

user_continue_ask = "y"

while user_continue_ask != "n":
    user_grade = int(input("What was your score?  "))
    if user_grade >= 97 and user_grade <= 100:
        print(f"A score of {user_grade} gives you a grade of A+")
    elif user_grade >= 93 and user_grade <= 96:
        print(f"A score of {user_grade} gives you a grade of A")
    elif user_grade >= 90 and user_grade <= 92:
        print(f"A score of {user_grade} gives you a grade of A-")
    elif user_grade >= 87 and user_grade <= 89:
        print(f"A score of {user_grade} gives you a grade of B+")         
    elif user_grade >= 83 and user_grade <= 86:
        print(f"A score of {user_grade} gives you a grade of B")        
    elif user_grade >= 80 and user_grade <= 82:
        print(f"A score of {user_grade} gives you a grade of B-")
    elif user_grade >= 77 and user_grade <= 79:
        print(f"A score of {user_grade} gives you a grade of C+")
    elif user_grade >= 73 and user_grade <= 76:
        print(f"A score of {user_grade} gives you a grade of C")
    elif user_grade >= 70 and user_grade <= 72:
        print(f"A score of {user_grade} gives you a grade of C-")
    elif user_grade >= 67 and user_grade <= 69:
        print(f"A score of {user_grade} gives you a grade of D+")
    elif user_grade >= 56 and user_grade <= 66:
        print(f"A score of {user_grade} gives you a grade of D")
    elif user_grade <= 55:
        print(f"A score of {user_grade} gives you a grade of F")
        
    user_continue_ask = input("Do you wish to continue? y/n:   ")
        




# Create a list of dictionaries where each dictionary represents a book that you have read. x
# Each dictionary in the list should have the keys title, author, and genre. x
# Loop through the list and print out information about each book. x

# Prompt the user to enter a genre, then loop through your books list and print out 
# the titles of all the books in that genre.

# three books: Tom Sawyer, Dune, Midshipman Quinn

book_dict = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction"
    },
    {
        "title": "Tom Sawyer",
        "author": "Mark Twain",
        "genre": "Adventure Fiction"        
    },
    {
        "title": "Midshipman Quinn",
        "author": "Showell Styles",
        "genre": "Historical Fiction" 
    }
]
    



# Loop through the list and print out information about each book.
for book in book_dict:
    print(book)





# Prompt the user to enter a genre, then loop through your books list and print out 
# the titles of all the books in that genre.

genre_pick = input("Pick a genre: ")

x = len(book_dict)

for i in range(0, x):
    if book_dict[i]["genre"] == genre_pick:
        print(book_dict[i]["title"])

