# Define a function that takes in a list of integers and a single integer as arguments. The single integer will represent an index point. The function needs to add the sum of all the numbers in the list up until and including the given index point by making use of recusion rather than loops.

# examples of input and output:

# adding_up_to([1, 2, 6, 8, 4, 9], 4)
# => 1 + 2 + 6 + 8 + 4 = 21


def adding_up_to(nums, index_point):
    if index_point < 0:
        return 0
    return nums[index_point] + adding_up_to(nums, index_point - 1)


# Ask the user to input numbers seperated by only a commas and convert it to a list of integers

print("Example list: '1,6,4,8,4,8,3'")
user_input = input("Please enter a list of numbers separated by commas: ")
try:
    num_list = [int(x.strip()) for x in user_input.split(",")]
    index_point = int(input("Please enter an index point: "))

    if index_point >= len(num_list):
        print("Index point out of range.")
    else:
        result = adding_up_to(num_list, index_point)
        print(f"The sum of numbers up to the index point is: {result}")

except ValueError:
    print("Invalid input. Please enter a list of numbers separated by commas.")
