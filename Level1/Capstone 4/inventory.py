from tabulate import tabulate


# ========The beginning of the class==========
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
        return (
            f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
        )


# =============Shoe list===========
shoe_list = []


# ==========Functions outside the class==============


def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            next(f)
            for line in f:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
        print("Data successfully read into shoe_list.")
        view_all()
    except Exception as e:
        print(f"Error: {e}")


def update_inventory():
    try:
        with open("inventory.txt", "w") as f:
            f.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                f.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"Error: {e}")


def capture_shoes():
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")

    while True:
        try:
            cost = float(input("Cost: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid float for cost.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    update_inventory()


def view_all():
    table = [str(shoe).split(", ") for shoe in shoe_list]
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"]))


def re_stock():
    min_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    restock = input(f"Do you want to restock {min_shoe.product} (y/n)? ")

    if restock.lower() == "y":
        while True:
            try:
                new_quantity = int(input("Enter new quantity: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for new quantity.")

        min_shoe.quantity += new_quantity
        update_inventory()


def search_shoe():
    code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return


def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: {value}")


def highest_qty():
    max_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(
        f"{max_shoe.product} is for sale with highest quantity: {max_shoe.get_quantity()}"
    )


# ==========Main Menu=============
while True:
    print(
        "\n1. Read Shoes Data\n2. Capture Shoes\n3. View All\n4. Re-Stock\n5. Search Shoe\n6. Value per Item\n7. Highest Quantity\n8. Exit"
    )
    choice = input("Choose an option: ")
    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        break
