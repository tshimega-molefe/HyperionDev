# PLEASE ENSURE YOU OPEN THIS FILE IN  VS CODE.

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them -- they are intended to be read by humans.
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.



# ========= Another elif example ===========
# elif is short for else if.
# It allows you to specify a new condition to test, if the first condition is False.

# ************ Example 1 ************
num_str = input("Enter a number, or enter 'NO' to stop the program: ")
if num_str == "2":
    num_int = int(num_str)
    #string input was cast to int
elif num_str == "3":
     num_int = int(num_str)
     #string input was cast to int 
else:
    print ("No can't be cast to an int.")
    #entering NO caused the print function to be executed.
    
# Entering anything other than 2, 3 or NO did not result in any output as the option was not defined in the code.
# Try creating processing instructions for other input, and adding output for every option

