# This program uses nested for and if-else loops to print an increasing number of asterisk characters in a range of 1 - 6, and then a decreasing amount until 1
star = "*"

for i in range(1, 11):
    if i <= 5:
        print(star * i)
    else:
        print(star * (10 - i))
