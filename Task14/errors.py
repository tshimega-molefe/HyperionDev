# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program \n")
# This was a syntax error, there were no parenthesis encompassing the string

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"
# value error - words cant be cased to integers
# NameError - The double equals is not the correct syntax to define the age_Str variable
age = int(age_Str)
# ValueError - The string variable was attemptting to be cast to a integer, only the string did not contain only numbers.
print(f"I'm {age} years old.")
# type error - cant concatenate age to string

# IndentationError - The errors above were due to an unexpected indentation

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# IndentationError - The errors above were due to an unexpected indentation

print(f"The total number of years: {total_years}")
# This was a syntax error, there were no parenthesis encompassing the string


# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = str((total_years * 12) + 6)

# TypeError: can only concatenate str (not "set") to str

# Name Error
print(f"In 3 years and 6 months, I'll be {total_months} months old")
# This was a syntax error, there were no parenthesis encompassing the string


# HINT, 330 months is the correct answer
