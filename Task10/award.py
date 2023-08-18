# define a function which finds the total time of the event, and returns the award received which corresponds to said event
def calculate_award(swimming_time, cycling_time, running_time):
    total_time = swimming_time + cycling_time + running_time

    if total_time <= 100:
        award = "Provincial Colors"
    elif 101 <= total_time <= 105:
        award = "Provincial Half Colors"
    elif 106 <= total_time <= 110:
        award = "Provincial Scroll"
    else:
        award = "No Award"

    return award


# Read input times in minutes for swimming, cycling, and running
swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

# Calculate the award
award = calculate_award(swimming_time, cycling_time, running_time)

# Display the total time and the award received
print(f"Total time taken: {swimming_time + cycling_time + running_time} minutes")
print(f"Award received: {award}")
