# The first programme reads in a string, and makes each alternate character an uppercase character, and each other alternate character a lowercase character
# The second programme reads in a string, and makes each alternate whord an uppercase character, and each other alternate word a lowercase character

# Program 1: Alternate Character Case Conversion
input_string_1 = input("Enter a string: ")
result_1 = ""
for i in range(len(input_string_1)):
    if i % 2 == 0:
        result_1 += input_string_1[i].upper()
    else:
        result_1 += input_string_1[i].lower()
print("Converted string for Program 1:", result_1)

# Program 2: Alternate Word Case Conversion
input_string_2 = input("Enter a sentance: ")
words_2 = input_string_2.split()
result_2 = []
for i in range(len(words_2)):
    if i % 2 == 0:
        result_2.append(words_2[i].upper())
    else:
        result_2.append(words_2[i].lower())
output_string_2 = " ".join(result_2)
print("Converted sentance for word conversion:", output_string_2)
