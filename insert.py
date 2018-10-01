import sqlite3

connection = sqlite3.connect("database.db")

print("Connected to the database successfully")

connection.execute(
    """
        INSERT INTO EMPLOYEES
        (
            ID,
            NAME,
            AGE,
            ADDRESS,
            SALARY
        )
        VALUES
        (
            2,
            "YETSOMEOTHERNAME",
            30,
            "33333 SOMETHING ST, SOMEWHERE",
            60000.00
        )
    """
)

connection.commit()

print("Inserted data successfully")

connection.close()