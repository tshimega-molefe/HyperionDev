### --- OOP Email Simulator --- ###


# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails.
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def read_status(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    email1 = Email("john.doe@example.com", "Hello", "This is a test email.")
    email2 = Email("jane.doe@example.com", "Meeting", "Let's schedule a meeting.")
    email3 = Email("admin@example.com", "Password Reset", "Reset your password.")
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)

    # Create 3 sample emails and add it to the Inbox list.


def list_emails():
    print("\nList of Emails:")
    for i, email in enumerate(inbox):
        read_status = "(Read)" if email.has_been_read else "(Unread)"
        print(f"{i + 1}. {email.subject_line} {read_status}")

    # Create a function which prints the email’s subject_line, along with a corresponding number.


def read_email(index):
    email = inbox[index]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    email.read_status()

    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.


populate_inbox()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
while True:
    user_choice = input(
        """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
    )

    try:
        user_choice = int(user_choice)
        if user_choice == 1:
            list_emails()
            selected_email = (
                int(input("Enter the number of the email you want to read: ")) - 1
            )
            if 0 <= selected_email < len(inbox):
                read_email(selected_email)
            else:
                print("Invalid selection.")

        elif user_choice == 2:
            list_emails()

        elif user_choice == 3:
            print("Quitting application.")
            break

        else:
            print("Oops - incorrect input.")

    except ValueError:
        print("Oops - incorrect input. Please enter a valid number.")
