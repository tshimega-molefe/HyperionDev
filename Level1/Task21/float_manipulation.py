import math
import statistics

# Initialize an empty list variable called numbers
numbers = []

# Request user input for float numbers while the length of numbers [] is less to 11
while len(numbers) < 10:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the total sum of the numbers in the numbers list
total_sum = sum(numbers)
print("Total Sum:", total_sum)


# Find the index of the largest number in the numbers list
largest_index = numbers.index(max(numbers))
print("Index of Largest Number:", largest_index)


# Find the index of the smallest number in the numbers list
smallest_index = numbers.index(min(numbers))
print("Index of Smallest Number:", smallest_index)


# Divide the total sum of the numbers by the count of items within the numbers list to find the average (rounded to 2 decimals)
average = round(total_sum / len(numbers), 2)
print("Average:", average)


# Find the median number within the numbers list

print("Median of data-set is : % s " % (statistics.median(numbers)))
