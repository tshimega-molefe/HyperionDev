# This programme displays a logical error.


def calculate_area(length, width):
    area = length * width
    return area


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = 7

# Swapping the variables to create a logical error
length, width = width, height

area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
