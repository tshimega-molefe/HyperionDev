# Using three inputs, ask the user to enter the names of three product strings.
# Using int(type) inputs, ask the user for product prices, set the variables to correspond to the product strings.
# Total Sum - price of three products added together.
# Average - total sum / count of products.
# Round this to two decimal places to set the avg price.
# Use the f string function to formulate the required sentence.
# The total of product1, product2, product3, is Rxx,xx and the average price of the items is Rxx,xx.


# Tell user what they're required to do

print("We need you to enter the names of three of your favourite products...")

product1 = str(input("Product one: ")).capitalize()
product2 = str(input("Product two: ")).capitalize()
product3 = str(input("Product three: ")).capitalize()

print("Please enter a price for each of the items...")

price1 = float(input(f"{product1} price: "))
price2 = float(input(f"{product2} price: "))
price3 = float(input(f"{product3} price: "))

total_cost = float(price1 + price2 + price3)

rounded_total_cost = round(total_cost, 2)

print(f"The total cost of your products is R{rounded_total_cost}.")

average = float(total_cost / 3)

rounded_average = round(average, 2)

print(f"The total cost of {product1}, {product2}, and {product3}, is R{rounded_total_cost}, and the average price of the items is R{rounded_average}.")


