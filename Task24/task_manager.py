from datetime import datetime


def read_users_from_file(filename):
    users = {}
    with open(filename, "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users


def reg_user(filename, users):
    new_username = input("Enter the username for the new user: ")
    if new_username in users:
        print("This username already exists.")
        return
    new_password = input("Enter the password for the new user: ")
    confirm_password = input("Confirm the password: ")
    if new_password != confirm_password:
        print("Passwords do not match.")
        return
    with open(filename, "a") as file:
        file.write(f"{new_username}, {new_password}\n")
    users[new_username] = new_password


def add_task(username, users):
    assigned_to = input("Enter the username of the person the task is assigned to: ")
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


def view_all(filename):
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
            print(
                f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
            )


def view_mine(filename, username):
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
            if assigned_to == username:
                print(
                    f"Assigned to: {assigned_to}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n"
                )


def mark_task_complete(filename, username):
    tasks = []
    with open(filename, "r") as file:
        for line in file:
            tasks.append(line.strip().split(", "))

    for i, task in enumerate(tasks):
        if task[0] == username and task[-1] == "No":
            print(
                f"Task {i + 1}:\nTitle: {task[1]}\nDescription: {task[2]}\nDue Date: {task[3]}\nStatus: {task[-1]}\n"
            )

    task_number = int(
        input("Select a task to mark as complete (-1 to return to main menu): ")
    )
    if task_number == -1:
        return

    task_to_mark = tasks[task_number - 1]
    task_to_mark[-1] = "Yes"

    with open(filename, "w") as file:
        for task in tasks:
            file.write(", ".join(task) + "\n")


def generate_reports():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    tasks_per_user = {}
    current_date = datetime.now().strftime("%Y-%m-%d")

    with open("tasks.txt", "r") as file:
        for line in file:
            total_tasks += 1
            assigned_to, _, _, due_date, _, status = line.strip().split(", ")
            tasks_per_user[assigned_to] = tasks_per_user.get(assigned_to, 0) + 1
            if status == "Yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                if due_date < current_date:
                    overdue_tasks += 1

    with open("task_overview.txt", "w") as file:
        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed_tasks}\n")
        file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue tasks: {overdue_tasks}\n")
        file.write(
            f"Percentage incomplete: {(uncompleted_tasks / total_tasks) * 100:.2f}%\n"
        )
        file.write(f"Percentage overdue: {(overdue_tasks / total_tasks) * 100:.2f}%\n")

    with open("user_overview.txt", "w") as file:
        file.write(f"Total users: {len(tasks_per_user)}\n")
        file.write(f"Total tasks: {total_tasks}\n")
        for user, user_tasks in tasks_per_user.items():
            file.write(f"\nUser: {user}\n")
            file.write(f"Total tasks assigned: {user_tasks}\n")
            file.write(
                f"Percentage of total tasks: {(user_tasks / total_tasks) * 100:.2f}%\n"
            )
            # Additional percentages related to the user can be calculated here


def edit_task(filename, username):
    tasks = []
    with open(filename, "r") as file:
        for line in file:
            tasks.append(line.strip().split(", "))

    for i, task in enumerate(tasks):
        if task[0] == username and task[-1] == "No":
            print(
                f"Task {i + 1}:\nTitle: {task[1]}\nDescription: {task[2]}\nDue Date: {task[3]}\nStatus: {task[-1]}\n"
            )

    task_number = int(input("Select a task to edit (-1 to return to main menu): "))
    if task_number == -1:
        return

    task_to_edit = tasks[task_number - 1]
    new_assigned_to = input(
        f"Current assignment: {task_to_edit[0]}. Enter new assignment: "
    )
    new_due_date = input(f"Current due date: {task_to_edit[3]}. Enter new due date: ")

    task_to_edit[0] = new_assigned_to
    task_to_edit[3] = new_due_date

    with open(filename, "w") as file:
        for task in tasks:
            file.write(", ".join(task) + "\n")


def display_statistics():
    try:
        with open("task_overview.txt", "r") as file:
            print(file.read())
        with open("user_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        generate_reports()
        display_statistics()


def main():
    users = read_users_from_file("user.txt")
    while True:
        menu_option = input(
            "Please select one of the following options:\na - login\ne - exit\n: "
        ).lower()
        if menu_option == "a":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username not in users or users[username] != password:
                print("Invalid username or password.")
                continue
            while True:
                if username == "admin":
                    menu_option = input(
                        "Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit\n: "
                    ).lower()
                else:
                    menu_option = input(
                        "Please select one of the following options:\na - add task\nva - view all tasks\nvm - view my tasks\ne - edit task\nc - complete task\nex - exit\n: "
                    ).lower()
                if menu_option == "r":
                    reg_user("user.txt", users)
                elif menu_option == "a":
                    add_task(username, users)
                elif menu_option == "va":
                    view_all("tasks.txt")
                elif menu_option == "vm":
                    view_mine("tasks.txt", username)
                elif menu_option == "e":
                    edit_task("tasks.txt", username)
                elif menu_option == "c":
                    mark_task_complete("tasks.txt", username)
                elif menu_option == "gr":
                    generate_reports()
                elif menu_option == "ds":
                    display_statistics()
                elif menu_option == "ex":
                    print("Goodbye!")
                    return
                else:
                    print("Invalid option.")
        elif menu_option == "e":
            print("Goodbye!")
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
