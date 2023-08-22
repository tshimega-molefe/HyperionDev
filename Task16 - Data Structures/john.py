# The following programme takes in a users name as a string. While the name is not john, it appends the the entered text to an array/list of incorrect attempts.


incorrect_names = []  # empty array

user_input = ""

correct_name = "John".lower()  # ignore case sensitivty

while user_input != correct_name:
    user_input = str(input("Enter your name: ")).lower()
    incorrect_names.append(user_input)
    print(incorrect_names)
print("Success, you're the right person John. World ending protocol access granted :)")
