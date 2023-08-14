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

if is_Sunny and is_weekend and greater_than_20:
    print(
        f"Based on the current weather conditions, you should {short_sleeve}, {shorts}, and {cap}"
    )
elif not is_Sunny and not is_weekend and not greater_than_20:
    print(
        f"Based on the current weather conditions, you should {long_sleeve}, {jeans}, and {raincoat}"
    )
else:
    print(
        f"Based on the current weather conditions, you should {long_sleeve}, {jeans}, and {raincoat}"
    )
