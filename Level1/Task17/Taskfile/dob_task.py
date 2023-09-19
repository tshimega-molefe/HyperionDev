# This program reads a dob txt document, contained within the same folder.
# We are going to perform actions on the contents of the txt document called dob.txt
# Importing os to check which directory we're currently in.
# Initialize a list/array of names
# Try reading the document, if you get exceptions (errors); print the error to the user
# Then we will print two lists, one from the names array, the second from the dates list.
import os

print(os.getcwd())

dates = []
names = []
try:
    with open("../Taskfile/DOB.txt", "r+") as register:
        for line in register:
            parts = line.split()
            name = " ".join(parts[0:2])
            names.append(name)
            dob = " ".join(parts[2:5])
            dates.append(dob)
except FileNotFoundError:
    print("The file 'DOB.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Name:\n")

for name in names:
    print(name)

print("\n")

print("Birthdate:\n")
for dob in dates:
    print(dob)
