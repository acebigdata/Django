import sqlite3
import sys

def printDB():
    try:
        result = my_cursor.execute("SELECT * FROM Basic Info")

        for row in result:
            print("COMPANY NAME", row[0])
            print("EXCHANGE: TICKER", row[1])
    except sqlite3.OperationalError:
        print("Table Does not exist")

# Create a database
db_conn = sqlite3.connect("test.db")
print("Database Created")

# Traverse through query
my_cursor = db_conn.cursor()

# To delete a table
# db_conn.execute("DROP TABLE IF EXIST Info")
# db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Info(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Company TEXT NOT NULL, Ticker TEXT NOT NULL);")
except sqlite3.OperationalError:
    print("Table Couldn't be created")
db_conn.commit()
print("Table Created")

db_conn.execute("INSERT INTO Info (Company, Ticker) VALUES ('Wal-Mart Stores', 'NYSE:WMT')")
db_conn.execute("INSERT INTO Info (Company, Ticker) VALUES ('Exxon Mobile', 'NYSE:XOM')")
db_conn.execute("INSERT INTO Info (Company, Ticker) VALUES ('Exxon Mobile', 'NYSE:XOM')")
db_conn.commit()

printDB()

# close database
db_conn.close()
print("Database Closed")
