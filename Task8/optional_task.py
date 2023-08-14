# TODO: Calculate monthly wage, for two different types of employees

# =================== VARIABLES ==================== #

# is_manager
# is_sales_person
# commission_rate
# gross_sales
# fixed_salary
# hourly_rate
# hours_worked

# =================== INPUTS ==================== #

# is user manager or a sales person

# if user is sales person, ask for gross sales for the month

# if user is manager, ask for number of hours worked for the month

# =================== LOGIC ==================== #

# find monthly wage based on user input

# =================== OUTPUT ==================== #

# print the total monthly wage for the user

# =================== VARIABLES ==================== #

is_manager = False
is_sales_person = False
commission_rate = 0.08
fixed_salary = 2_000
hourly_rate = 40

# =================== INPUTS ==================== #

employee_type = str(input("Are you a manager? ('Yes'/'No'): ")).lower()
if employee_type == "yes":
    is_manager = True
    is_sales_person = False
else:
    is_manager = False
    is_sales_person = True

if is_sales_person == True:
    gross_sales = float(input("Please enter your gross sales for the month: "))
    round(gross_sales, 2)
    month_wage = (gross_sales * commission_rate) + fixed_salary
if is_manager == True:
    hours_worked = int(
        input("Please enter your number of hours worked for the month: ")
    )
    month_wage = hours_worked * hourly_rate

# =================== OUTPUT ==================== #

print(f"Your total monthly wage is: {month_wage}")
