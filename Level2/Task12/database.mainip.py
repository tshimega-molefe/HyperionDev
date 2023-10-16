# import SQLite
import sqlite3

# create a database sqlite3 connection
db = sqlite3.connect("python_programming")

# create cursor
cursor = db.cursor()

print(
    "Database connection established.\n"
)  # This might need to be put into a trycatch for error handling of the db conection.

# Create the 'python_programming' table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
"""
)

print("Table Created")  # validation comment

# Insert new rows into the 'python_programming' table
data_to_insert = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99),
]

cursor.executemany(
    "INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)", data_to_insert
)

print("- Students added")  # validation comment

# Select all records with a grade between 60 and 80
cursor.execute(
    """
SELECT * FROM python_programming
WHERE grade BETWEEN 60 AND 80
"""
)
results = cursor.fetchall()
print("Records with grade between 60 and 80:")
for row in results:
    print(row)

# Change Carl Davis's grade to 65
cursor.execute(
    """
UPDATE python_programming
SET grade = 65
WHERE name = 'Carl Davis'
"""
)

#  Delete Dennis Fredrickson's row
cursor.execute(
    """
DELETE FROM python_programming
WHERE name = 'Dennis Fredrickson'
"""
)

# Change the grade of all students with an id greater than 55 to 80
cursor.execute(
    """
UPDATE python_programming
SET grade = 80
WHERE id > 55
"""
)

# Commit the changes and close the connection
db.commit()
db.close()
