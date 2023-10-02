# Define the Adult class
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


# Define the Child class as a subclass of Adult
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


# Take user inputs
name = input("Enter the name: ")
age = int(input("Enter the age: "))
eye_colour = input("Enter the eye colour: ")
hair_colour = input("Enter the hair colour: ")

# Create an instance of either Adult or Child based on the age
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
else:
    person = Child(name, age, eye_colour, hair_colour)

# Call the can_drive() method
person.can_drive()
