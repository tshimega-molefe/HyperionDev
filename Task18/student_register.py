# We're writing a program that allows a user to register a student for an exam venue
# We first need to ask the user to input how many students are registering with a str(input())
# Store this in a variable "number_of_students"
# Then we're creating a "for" loop which runs for "as long as the number_of_students registered"
# For each iteration of this for loop, as the user to input a student number with an int(input())
# Store this in a variable "student_number"
# Then write this student_number to a new file, reg_form.txt
# Ensure you append the string of "_________________" to each student number to enable users to sign this dotted line in real life when this document is printed.

number_of_students = int(
    input("Please enter the number of students registering this year: ")
)

print(f"Excellent! Expect {number_of_students} students on opening day")

with open("reg_form.txt", "w") as file:
    for _ in range(number_of_students):
        student_number = input("Please enter the student number: ")

        file.write((student_number) + "_________________\n")


print("Registration completed and student numbers saved to reg_form.txt.")
