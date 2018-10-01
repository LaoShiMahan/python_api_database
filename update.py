import sqlite3

connection = sqlite3.connect("database.db")

print("Connected to the database successfully")

connection.execute(
    """
        UPDATE EMPLOYEES
        SET SALARY = 110000.00
        WHERE ID = 0
    """
)

connection.commit()

print("Total updates: ", connection.total_changes)

print("Database updated successfully")

connection.close()