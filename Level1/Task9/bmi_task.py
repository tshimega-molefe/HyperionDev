weight = float(input("Please enter your weight: "))

height = float(input("Please enter your height: "))

bmi = round((weight / height**2), 2)

classification = ""

if bmi > 30:
    classification += "you're clinically classified as obese unfortunately."
elif bmi > 25:
    classification += "you're clinically classified as overweight."

elif bmi > 18.5:
    classification += "you're clinically classified as normal."

else:
    classification += "you're clinically classified as underweight."


print(f"Your BMI is {bmi}, and {classification}")
