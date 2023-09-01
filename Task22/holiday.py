# Function to calculate hotel cost
def hotel_cost(num_nights):
    per_night_charge = 150
    return num_nights * per_night_charge


# Function to calculate plane cost
def plane_cost(city_flights):
    # Define prices based on the chosen city
    city_flights = city_flights.lower()
    if city_flights == "cape town":
        return 500
    elif city_flights == "johannesburg":
        return 400
    elif city_flights == "durban":
        return 350
    else:
        return 0  # Return 0 for invalid options


# Function to calculate car rental cost
def car_rental_cost(rental_days):
    daily_rental_cost = 50
    return rental_days * daily_rental_cost


# Function to calculate total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental_cost):
    return hotel_cost + plane_cost + car_rental_cost


# Main program
destination_options = ["cape town", "johannesburg", "durban"]

print("Welcome to the Holiday Cost Calculator!")

while True:
    destination = (
        input("Enter your destination (Cape Town, Johannesburg, or Durban): ")
        .strip()
        .lower()
    )

    if destination not in destination_options:
        print("Invalid destination choice. Please choose from the provided options.")
    else:
        break

num_nights = int(input("Enter the number of nights you will be staying: "))

while True:
    rental_days = int(input("Enter the number of days you will be renting a vehicle: "))

    if rental_days > num_nights:
        print(
            "The number of rental days cannot be longer than the number of nights you are staying."
        )
    else:
        break

hotel_cost_value = hotel_cost(num_nights)
plane_cost_value = plane_cost(destination)
car_rental_cost_value = car_rental_cost(rental_days)
total_cost = holiday_cost(hotel_cost_value, plane_cost_value, car_rental_cost_value)

print("\nHoliday Details:")
print(f"Destination: {destination.capitalize()}")
print(f"Number of Nights: {num_nights}")
print(f"Number of Rental Days: {rental_days}")
print(f"Hotel Cost: ${hotel_cost_value}")
print(f"Plane Cost: ${plane_cost_value}")
print(f"Car Rental Cost: ${car_rental_cost_value}")
print(f"Total Holiday Cost: ${total_cost}")
