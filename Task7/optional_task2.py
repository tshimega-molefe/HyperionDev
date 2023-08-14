# Definitions
greater_than_20 = False
is_weekend = False
is_Sunny = False
short_sleeve = "wear a short sleeve"
long_sleeve = "wear a long sleeve"
shorts = "wear shorts"
jeans = "wear jeans"
cap = "wear a cap"
raincoat = "wear a raincoat"

# Inputs
temp = int(input("What is the current temperature outside?: "))

weekend = str(input("Is it the weekend? 'Yes' or 'No': ")).lower()
if weekend == "yes":
    is_weekend = True

sunny = str(input("Is it sunny outside? 'Yes' or 'No': ")).lower()
if sunny == "yes":
    is_Sunny = True

# Conditional logic
if temp > 20:
    greater_than_20 = True

outfit = ""

if greater_than_20:
    outfit += short_sleeve
else:
    outfit += long_sleeve

if is_weekend:
    outfit += ", " + shorts
else:
    outfit += ", " + jeans

if is_Sunny:
    outfit += ", " + cap
else:
    outfit += ", " + raincoat

# Output/Display to User

print(f"Based on the current weather conditions, you should {outfit}.")
