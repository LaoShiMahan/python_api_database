import sqlite3

connection = sqlite3.connect("database.db")

print("Connected to the database successfully")

# connection.execute(
#     "BEGIN;"
# )

# print("BEGIN successful")

connection.execute(
    """
        DELETE
        FROM EMPLOYEES
        WHERE ID = 0;
    """
)

print("DELETE successful")

# connection.execute(
#     "ROLLBACK;"
# )

# print("ROLLBACK successful")

connection.commit()

print("Total updates: ", connection.total_changes)

print("Database updated successfully")

connection.close()