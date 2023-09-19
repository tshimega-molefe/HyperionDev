num1 = input("Enter number one: ")
num2 = input("Enter number two: ")

print("Before swap: Num1 = {} Num2 = {}".format(num1, num2))

# create a copy of number 1
a = num1

# set number 1 to number 2
num1 = num2

# set number 2 to the copy of number 1
num2 = a

print("After swap: Num1 = {} Num2 = {}".format(num1, num2))

