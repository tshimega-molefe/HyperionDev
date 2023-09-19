# Request from the user using an input command for each item, asking for name: string, age: number, house_number: number, and street_name: string
# We have denoted the variable type, after the colon `:`
# Using the format method, print out the details within a single sentence, in the form print("This is {}, He is {} years old, and lives at house number {} on {}."format(name, age, house_number, street_name))

print("Please enter your particular user details below...")

name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

print("Hello {}! We see that you're {} years old. Your physical address is {} {}.".format(name, age, house_number, street_name))