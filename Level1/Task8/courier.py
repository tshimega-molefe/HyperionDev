# We're trying to calculate the cost of sending a parcel for a courier company.
# The variables to consider are:
# Distance
# Freight
# Insurance
# Gift
# Priority
# Parcel

# Create an algorithm using these variables to find the total cost, stored as
# total_cost = freight + insurance + gift + priority + parcel

# variables

# freight
air_cost = 0.36
land_cost = 0.25

# insurance
full = 50.00
limited = 25.00

# gift
cover = 15.00
no_cover = 0.00

# priority
priority_amount = 100.00
standard = 20.00

# parcel
sleeve = 100
box = 150


# error handling
freight_error = (
    "OOPS! You didn't enter the correct text (Please enter 'air' or 'land'): "
)
insurance_error = (
    "OOPS! You didn't enter the correct text (Please enter 'full' or 'limited'): "
)

gift_error = "OOPS! You didn't enter the correct text (Please enter 'yes' or 'no'): "
priority_error = (
    "OOPS! You didn't enter the correct text (Please enter 'priority' or 'standard'): "
)

parcel_error = (
    "OOPS! You didn't enter the correct text (Please enter 'sleeve' or 'box'): "
)


# Inputs

distance = float(input("Enter the total distance of the delivery in kilometers: "))
print(f"You entered a distance of: {distance}")


freight = str(
    input("Are you sending an air or land parcel? (Eneter 'air' or 'land'): ")
).lower()
if freight == "air":
    freight_cost = distance * air_cost
elif freight == "land":
    freight_cost = distance * land_cost
else:
    freight = str(input(freight_error)).lower()

print(f"Your freight cost is: {freight_cost}")


insurance = str(
    input(
        "Do you need full or limited insurance? (Enter 'full' or 'limited'): "
    ).lower()
)
if insurance == "full":
    insurance_cost = full
elif insurance == "limited":
    insurance_cost = limited
else:
    insurance = str(input(insurance_error).lower())
print(f"Your insurance cost is: {insurance_cost}")


gift = str(input("Do you need gift cover? (Enter 'yes' or 'no'): ")).lower()
if gift == "yes":
    gift_cost = cover
elif gift == "no":
    gift_cost = no_cover
else:
    gift = str(input(gift_error)).lower()
print(f"Your gift cost is: {gift_cost}")


priority = str(
    input(
        "Do you want priority or standard devivery? (Enter 'priority' or 'standard'): "
    )
).lower()
if priority == "priority":
    priority_cost = priority_amount
elif priority == "standard":
    priority_cost = standard
else:
    priority = str(input(priority_error)).lower()
print(f"Your priority cost is: {priority_cost}")


parcel = str(
    input(
        "Do you want to use a parcel sleeve or parcel box? (Enter 'sleeve' or 'box'): "
    ).lower()
)
if parcel == "sleeve":
    parcel_cost = sleeve
elif parcel == "box":
    parcel_cost = box
else:
    parcel = str(input(parcel_error).lower())
print(f"Your parcel cost is: {parcel_cost}")


total_cost = freight_cost + insurance_cost + gift_cost + priority_cost + parcel_cost
round(total_cost, 2)

print(f"The total cost of sending your parcel is R{total_cost}")
