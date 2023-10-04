# Defining the Shoe class with required methods
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# List to store shoe objects
shoe_list = []


# Function to read shoe data from a text file and populate the shoe_list
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
    except Exception as e:
        print(f"An error occurred: {e}")


def update_inventory_file():
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")  # Writing the header
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")


# Function to restock shoes with the lowest quantity
def re_stock():
    min_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Lowest quantity shoe: {min_shoe}")
    restock_qty = int(input("Enter the quantity to restock: "))
    min_shoe.quantity += restock_qty
    update_inventory_file()  # Update the inventory file


# Function to view all shoes
def view_all():
    for shoe in shoe_list:
        print(shoe)


# Function to capture new shoe data
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    update_inventory_file()


# Function to search for a shoe by code
def search_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None


# Function to calculate the total value for each item
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Total value of {shoe.product}: {value}")


# Function to find the shoe with the highest quantity
def highest_qty():
    max_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"Highest quantity shoe: {max_shoe}")


read_shoes_data()

# Main Menu
while True:
    print("1. Capture Shoes")
    print("2. View All")
    print("3. Restock")
    print("4. Search by Code")
    print("5. Calculate Value Per Item")
    print("6. Find Highest Quantity Shoe")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        capture_shoes()
    elif choice == 2:
        view_all()
    elif choice == 3:
        re_stock()
    elif choice == 4:
        code = input("Enter the shoe code to search: ")
        shoe = search_shoe(code)
        if shoe:
            print(shoe)
        else:
            print("Shoe not found.")
    elif choice == 5:
        value_per_item()
    elif choice == 6:
        highest_qty()
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please try again.")
