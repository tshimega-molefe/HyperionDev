# Define a function that returns the largest number in a list of integers taken as an argument. The problem needs to be solves using recusion, and not loops.


def find_largest(nums, index=0, largest=None):
    if index == len(nums):
        return largest
    if largest is None or nums[index] > largest:
        largest = nums[index]
    return find_largest(nums, index + 1, largest)


# Ask the user for input and convert it to a list of integers
print("Example list: '3,7,1,23,17,5'")
user_input = input("Please enter a list of numbers separated by commas: ")
try:
    num_list = [int(x.strip()) for x in user_input.split(",")]

    if len(num_list) == 0:
        print("The list should contain at least one number.")
    else:
        result = find_largest(num_list)
        print(f"The largest number in the list is: {result}")

except ValueError:
    print("Invalid input. Please enter a list of numbers separated by commas.")
