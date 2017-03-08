## Full walkthrough of sqlite3 with python
import sqlite3
import sys

def printDB():
    try:
        result = my_cur.execute("SELECT * FROM Employees")
        for row in result:
            print("ID: ", row[0])
            print("First Name: ", row[1])
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Address: ", row[4])
            print("Salary: ", row[5])
            print("Hire Date: ", row[6])

    except sqlite3.OperationalError:
        print("Table does not exist")
    except:
        print("Couldn't retrieve data from database")

# Create a connection/Create a new database if not created
db_conn = sqlite3.connect('test.db')
print ("Database Connection Established")

# Create cursor to traverse the results of the database
my_cur = db_conn.cursor()

# Drop/Delete a table
# db_conn.execute("DROP TABLE IF EXISTS Employees")
# db_conn.commit()
# print("Table Deleted")

# Execute a SQL command
## Create a TABLE
try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Fname TEXT NOT NULL, Lname TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    # Commit the command above
    db_conn.commit()
    print("Table Created")

except sqlite3.OperationalError:
    print("Table Couldn't be Created")

## Insert a row
db_conn.execute("INSERT INTO Employees(Fname, Lname, Age, Address, Salary, HireDate) VALUES('Isaac', 'Zhou', 32, 'New York, NY' ,5000000, date('now'))")
db_conn.commit()

## Update row and value
try:
    db_conn.execute("UPDATE Employees SET Address = 'Hawaii' WHERE ID = 1")
    db_conn.execute("UPDATE Employees SET Profile = 'acebigdata' WHERE ID = 1")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")

## Delete a row
try:
    db_conn.execute("DELETE FROM Employees WHERE ID = 2")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Cannot delete the row")

## Roll back/recall the last command
db_conn.rollback()

## Add a column
try:
    db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Profile' TEXT")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table couldn't be updated")

## Retrieve database table names
my_cur.execute("PRAGMA TABLE_INFO(Employees)")

## Use fetch all to get all the rows/data
rowNames = [nameTuple[1] for nameTuple in my_cur.fetchall()]
print(rowNames)

printDB()

## Get the total rows in  the database
print("***********************************************")
print("Get the total number of rows in the database")
my_cur.execute("SELECT COUNT(*) FROM Employees")
num_of_row = my_cur.fetchall()
print("Total Rows:", num_of_row[0][0])

## Get the sqlite version
print("***********************************************")
my_cur.execute("SELECT SQLITE_VERSION()")
print("SQLite Verion:", my_cur.fetchall()[0][0])

## Dictionary database
print("***********************************************")
with db_conn:
    db_conn.row_factory = sqlite3.Row
    my_cur = db_conn.cursor()
    my_cur.execute("SELECT * FROM Employees")
    my_rows = my_cur.fetchall()
    for row in my_rows:
        print("{a} {b}".format(a = row["Fname"], b = row["Lname"]))

## Write data to a file
print("***********************************************")
with open("dump.sql", "w+") as f:
    for line in db_conn.iterdump():
        f.write("{a}\n".format(a = line))
# Close the database connection after use
db_conn.close()
print("***********************************************")
print("Close the Database Connection")
