# The following programme executes a while loop, which requests for the user to enter integers as inputs, for as long as the number they enter is not -1. While doing so, the count, and total sum of numbers entered by the user is being stored, and summed respectively upon for as long the while loop executes.

total_sum = 0
count = 0
stop_while = 0

while stop_while != 23:
    user_input = int(input("Please enter an integer: "))
    stop_while = user_input

    total_sum += user_input
    count += 1

if count > 0:
    average = total_sum / count
    print(f"Average of entered numbers is equal to {average}.")
else:
    print("No numbers were entered")
