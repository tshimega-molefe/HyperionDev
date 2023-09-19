# Initialize an empty list variable called menu
menu = []

# Request user input for menu items while the length of menu is less than or equal to 4

print("The cafe menu is currently empty, please enter at least four items below.")

while len(menu) <= 3:
    menu_item = input("Enter a menu item: ")
    menu.append(menu_item)

# Initialize an empty dictionary variable called stock
stock = {}

# Request user input for stock values for each item in the menu
for item in menu:
    stock[item] = int(input(f"Enter the stock number value for {item}: "))

# Initialize an empty dictionary variable called price
price = {}

# Request user input for prices for each item in the menu
for item in menu:
    price[item] = float(input(f"Enter the price for {item}: "))

# Calculate the total stock value in the cafe
total_stock_value = sum(stock[item] * price[item] for item in menu)

# Print the total stock value
print(f"Total stock value in the cafe: R{total_stock_value}")
