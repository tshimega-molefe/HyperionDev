# Initialize two inputs for the users first name, and second name.
# Concatenate both variables into a full name variable.
# Check to see if the full name variable is empty, and return the appropriate error message.
# Check the length of the full name variable, and if its less than or equal to 4, return an error.
# Check the length of the full name variable, and if its greater than or equal to 25, return an error.

first_name = str(input("Enter your first name: ")).capitalize()
last_name = str(input("Enter your last name: ")).capitalize()

full_name = str(first_name + " " + last_name)

name_length = len(full_name)

if name_length == 0:
    print("You haven't entered anything. Please enter your full name.")

if name_length <= 4:
    print(
        "You have entered less than 4 characters. Please make sure that you have entered your name and surname."
    )

if name_length >= 25:
    print(
        "You have entered more than 25 characters. Please make sure that you have only entered your full name."
    )

if name_length > 4 and name_length < 25:
    print("Thank you for entering your name.")
