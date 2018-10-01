import sqlite3

connection = sqlite3.connect("database.db")

print("Connected to the database successfully")

connection.execute(
    """
        CREATE TABLE EMPLOYEES
        (
            ID       INT       PRIMARY KEY  NOT NULL,
            NAME     TEXT                   NOT NULL,
            AGE      INT                    NOT NULL,
            ADDRESS  CHAR(50)                       ,
            SALARY   REAL
        )
    """
)

print("Table created successfully")

connection.close()