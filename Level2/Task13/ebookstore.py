import sqlite3

# Connect to the database (create a new one if it doesn't exist)
conn = sqlite3.connect("ebookstore.db")
cursor = conn.cursor()

# Create the "book" table if it doesn't exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
"""
)

# Insert initial data with "INSERT OR IGNORE" to avoid duplicate unique constraint errors
initial_data = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12),
]

cursor.executemany(
    "INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)",
    initial_data,
)
conn.commit()


# Function to enter a new book into the database
def enter_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    qty = int(input("Enter the quantity: "))
    cursor.execute(
        "INSERT INTO book (title, author, qty) VALUES (?, ?, ?)", (title, author, qty)
    )
    conn.commit()


# Function to update the quantity of an existing book
def update_book():
    book_id = int(input("Enter the book ID to update: "))
    new_qty = int(input("Enter the new quantity: "))
    cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (new_qty, book_id))
    conn.commit()


# Function to delete a book from the database
def delete_book():
    book_id = int(input("Enter the book ID to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
    conn.commit()


# Function to search for books based on a keyword in the title or author
def search_books():
    keyword = input("Enter a keyword to search for books: ")
    cursor.execute(
        "SELECT * FROM book WHERE title LIKE ? OR author LIKE ?",
        (f"%{keyword}%", f"%{keyword}%"),
    )
    books = cursor.fetchall()
    if books:
        for book in books:
            print(
                f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}"
            )
    else:
        print("No books found matching the keyword.")


while True:
    print("Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_books()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

# Close the connection when done
conn.close()
