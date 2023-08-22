import math

print("investment - To calculate the amount of interest you'll earn on your investment")
print("bond - To calculate the amount you'll have to pay on a home loan")

# Request user's choice and ensure it's valid
calculator = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: "
).lower()

while calculator != "investment" and calculator != "bond":
    print("You didn't enter the correct text, please try again... ")
    calculator = input(
        "Enter either 'investment' or 'bond' from the menu above to proceed: "
    ).lower()

if calculator == "investment":
    try:
        amount = float(
            input("Enter the amount you're depositing into your investment account: R")
        )
        rate = float(input("Enter the interest rate (Do not enter the % symbol): "))
        years = int(input("Enter the number of years you plan on investing: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        exit(1)  # Try failed, catch returns error

    interest = input(
        "Enter either 'simple' or 'compound' from the menu above to proceed: "
    ).lower()

    if interest == "simple":
        total_simple = amount * (1 + ((rate / 100) * years))
        print(
            f"The total amount you will receive from your simple interest investment is R{total_simple}"
        )
    elif interest == "compound":
        total_compound = amount * math.pow((1 + (rate / 100)), years)
        print(
            f"The total amount you will receive from your compound interest investment is R{total_compound}"
        )
    else:
        print("Invalid option selected for interest calculation.")
elif calculator == "bond":
    try:
        present_value = float(input("Enter the present value of the house: R"))
        rate = float(input("Enter the interest rate (Do not enter the % symbol): "))
        months = int(input("Enter the number of months you plan to repay the bond: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        exit(1)  # Try failed, catch returns error

    repayment = round(
        ((rate / 12) * present_value) / (1 - math.pow((1 + (rate / 12)), -months)), 2
    )
    total_cost = round((repayment + present_value), 2)

    print(f"The total monthly repayment on your home loan will be R{repayment}")
    print(
        f"Upon completion of the repayment period, you would have spent R{total_cost}"
    )
