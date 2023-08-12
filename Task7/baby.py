# Request for the user to enter an int value for the year they were born.
# We will be initializing a variable of entry_permitted, which will only be true, if the year the user was born, is less than 18 years prior to 2023 (i.e. 2005 or less)
# If entered age_year is less than or equal to 2005, or less than 2004, then print the message to the user that they're old enough.
yob = int(input("Which year were you born: "))

entry_permitted = False

if yob <= 2005:
    entry_permitted = True
    print("Congrats you are old enough.")
