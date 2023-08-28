from datetime import datetime

# Initialize an empty dictionary to store username data
users = {}
total_users = 0
total_tasks = 0

# Read user data from a file and populate the users dictionary
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(",")
        users[username] = password

# Infinite loop to display the main menu
while True:
    # Display the menu options and get user input
    menu = input(
        """Select one of the following options:
a - login
e - exit
: """
    ).lower()

    if menu == "a":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in users or users[username] != password:
            print("Invalid username or password.")
            continue

        if username == "admin":
            while True:
                admin_menu = input(
                    """Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view statistics
e - exit
: """
                ).lower()

                if admin_menu == "r":
                    new_username = input("Enter a new username: ")
                    if new_username in users:
                        print("Username already exists.")
                        continue

                    while True:
                        new_password = input("Enter a new password: ")
                        confirm_password = input("Confirm the password: ")

                        if new_password != confirm_password:
                            print("Passwords do not match. Please try again.")
                        else:
                            break

                    users[new_username] = new_password
                    with open("user.txt", "a") as file:
                        file.write(f"{new_username},{new_password}\n")
                    total_users += 1
                    print("User registered successfully.")

                elif admin_menu == "a":
                    assigned_to = input(
                        "Enter the username of the person the task is assigned to: "
                    )

                    if assigned_to not in users:
                        print("User not found. Task cannot be added.")
                        continue

                    title = input("Enter the title of the task: ")
                    description = input("Enter the description of the task: ")
                    due_date = input("Enter the due date of the task: ")
                    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    with open("tasks.txt", "a") as file:
                        file.write(
                            f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n"
                        )
                    total_tasks += 1
                    print("Task added successfully.")

                # View all tasks option
                elif admin_menu == "va":
                    with open("tasks.txt", "r") as file:
                        for line in file:
                            (
                                assigned_to,
                                title,
                                description,
                                due_date,
                                current_date,
                                status,
                            ) = line.strip().split(", ")
                            print(
                                f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                            )

                # View specific username tasks option
                elif admin_menu == "vm":
                    logged_in_user = input(
                        "Enter the username of the person whose tasks you want to find: "
                    )

                    if logged_in_user not in users:
                        print("User does not exist.")
                        continue

                    tasks_found = False
                    with open("tasks.txt", "r") as file:
                        for line in file:
                            (
                                assigned_to,
                                title,
                                description,
                                due_date,
                                current_date,
                                status,
                            ) = line.strip().split(", ")
                            if assigned_to == logged_in_user:
                                tasks_found = True
                                print(
                                    f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                                )

                    if not tasks_found:
                        print("No tasks found for this user.")

                elif admin_menu == "s":
                    with open("user.txt", "r") as user_file:
                        total_users = len(user_file.readlines())

                    with open("tasks.txt", "r") as tasks_file:
                        total_tasks = len(tasks_file.readlines())

                    print(f"Total Users: {total_users}\nTotal Tasks: {total_tasks}\n")

                elif admin_menu == "e":
                    print("Goodbye!!!")
                    exit()

                else:
                    print("You have entered an invalid input. Please try again")
        else:
            while True:
                user_menu = input(
                    """Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: """
                ).lower()

                if user_menu == "a":
                    assigned_to = username

                    if assigned_to not in users:
                        print("User not found. Task cannot be added.")
                        continue

                    title = input("Enter the title of the task: ")
                    description = input("Enter the description of the task: ")
                    due_date = input("Enter the due date of the task: ")
                    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    with open("tasks.txt", "a") as file:
                        file.write(
                            f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n"
                        )
                    print("Task added successfully.")

                elif user_menu == "va":
                    with open("tasks.txt", "r") as file:
                        for line in file:
                            (
                                assigned_to,
                                title,
                                description,
                                due_date,
                                current_date,
                                status,
                            ) = line.strip().split(", ")
                            print(
                                f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                            )

                elif user_menu == "vm":
                    tasks_found = False
                    with open("tasks.txt", "r") as file:
                        for line in file:
                            (
                                assigned_to,
                                title,
                                description,
                                due_date,
                                current_date,
                                status,
                            ) = line.strip().split(", ")
                            if assigned_to == username:
                                tasks_found = True
                                print(
                                    f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                                )

                    if not tasks_found:
                        print("No tasks found for this user.")

                elif user_menu == "e":
                    print("Goodbye!!!")
                    exit()

                else:
                    print("You have entered an invalid input. Please try again")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have entered an invalid input. Please try again")
