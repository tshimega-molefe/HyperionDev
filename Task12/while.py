# The following programme executes a while loop, which requests for the user to enter integers as inputs, for as long as the number they enter is not -1. While doing so, the count, and total sum of numbers entered by the user is being stored, and summed respectively upon for as long the while loop executes.

total_sum = 0
count = 0
user_input = 0  # Initialize user_input with a non-terminating value

while user_input != -1:
    user_input = int(input("Please enter an integer: "))

    if user_input != -1:  # Exclude -1 from calculations
        total_sum += user_input
        count += 1

if count > 0:
    average = total_sum / count
    print(f"Average of entered numbers is equal to {average:.2f}.")
else:
    print("No numbers were entered")
