# Request for the user to input a name for their favorite restaurant, and store this as `string_fav`

# Request for the user to input a number for their favorite number, and store this as `int_fav`

# Print string_fav

# Print int_fav

# Incorrectly cast string_fav to an type(int), and add comments to explain why it fails.

string_fav = str(input("Please enter the name of your favourite restaurant: "))
int_fav = int(input("Please enter your favourite number: "))

print(string_fav)
print(int_fav)


int_string = int(string_fav)

# We return an error due to a variable of type string, being assigned a type of int; this causes an error as the incorrect literal of int, is being cast onto a string variable. Had the code above been `int_string = str(string_fav)`, the code would have executed correctly.

print(int_string)


