import sqlite3

connection = sqlite3.connect("database.db")

print("Connected to the database successfully")

data = connection.execute(
    """
        SELECT
            ID,
            NAME,
            AGE,
            ADDRESS,
            SALARY
        FROM EMPLOYEES
    """
)

for row in data:
    print("     ID  =  ", row[0])
    print("   NAME  =  ", row[1])
    print("    AGE  =  ", row[2])
    print("ADDRESS  =  ", row[3])
    print(" SALARY  =  ", row[4])
    print("\n")

print("Selected data successfully")

connection.close()