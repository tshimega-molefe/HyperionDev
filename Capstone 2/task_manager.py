from datetime import datetime


def read_users_from_file(filename):
    users = {}
    is_file_empty = True

    with open(filename, "r") as file:
        for line in file:
            is_file_empty = False
            username, password = line.strip().split(", ")
            users[username] = password

    # If the file is empty or admin is not registered, add admin to the file
    if is_file_empty or "admin" not in users:
        users["admin"] = "admin"
        with open(filename, "a") as file:
            file.write(f"admin, admin\n")

    return users


def display_menu(options):
    print("Select one of the following options:")
    print("\n".join(options))
    return input(": ").lower()


def process_task_input(username, users):
    assigned_to = (
        username
        if username == "admin"
        else input("Enter the username of the person the task is assigned to: ")
    )
    if assigned_to not in users:
        print("User not found. Task cannot be added.")
        return

    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    current_date = datetime.now().strftime("%Y-%m-%d")

    with open("tasks.txt", "a") as file:
        file.write(
            f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n"
        )
    print("Task added successfully.")


def display_tasks(filename, username=None):
    tasks_found = False
    with open(filename, "r") as file:
        for line in file:
            (
                assigned_to,
                title,
                description,
                due_date,
                current_date,
                status,
            ) = line.strip().split(", ")
            if username is None or assigned_to == username:
                tasks_found = True
                print(
                    f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                )

    if not tasks_found:
        print(f"No tasks found for {username if username else 'any user'}.")


def main():
    users = read_users_from_file("user.txt")
    logged_in_user = None

    while True:
        menu = display_menu(["a - login", "e - exit"])

        if menu == "a":
            if logged_in_user:
                print(f"Welcome back, {logged_in_user}!")
            else:
                username = input("Enter your username: ")
                password = input("Enter your password: ")

            if username not in users or users[username] != password:
                print("Invalid username or password.")
                continue

            logged_in_user = username

            while True:
                options = [
                    "a - add task",
                    "va - view all tasks",
                    "vm - view my tasks",
                    "e - exit",
                ]
                if logged_in_user == "admin":
                    options.extend(["r - register a user", "s - view statistics"])

                user_menu = display_menu(options)

                if user_menu == "a":
                    process_task_input(logged_in_user, users)
                elif user_menu == "va":
                    display_tasks("tasks.txt")
                elif user_menu == "vm":
                    display_tasks("tasks.txt", username=logged_in_user)
                elif user_menu == "r":
                    print("Registering a user (not implemented).")
                elif user_menu == "s":
                    print("Showing statistics (not implemented).")
                elif user_menu == "e":
                    print("Goodbye!!!")
                    exit()
                else:
                    print("You have entered an invalid input. Please try again.")
        elif menu == "e":
            print("Goodbye!!!")
            exit()
        else:
            print("You have entered an invalid input. Please try again.")


if __name__ == "__main__":
    main()
