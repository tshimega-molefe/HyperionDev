# Request from the user to enter three different numbers; use an input.
# Ensure you're assigning the input to descriptive variables for each number.
# Print the sum of all three number variables, set to variable total_sum
# Initialize a variable called difference, set it equal to num1 - num3; print a message to explain what this number is.
# Initialize a variable called multiply, set it equal to num3 times (*) num1, print a message to explain what this number is.
# Calculate total_sum / num3

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

print(
    f"You entered {num1} as your first number, {num2} as your second, and {num3} as your third."
)

total_sum = num1 + num2 + num3

difference = num1 - num3

multiply = num3 * num1

print(f"The sum of the numbers you entered is {total_sum}")
print(
    f"The difference between the first number and the third number you entered is {difference}"
)
print(f"The product of your first and third number is {multiply}")

division_result = total_sum / num3
print(f"The result of dividing the total sum by the third number is: {division_result}")
