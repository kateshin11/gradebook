#python3 -m pip install mysql-connector-python
#python3 -m pip install PrettyTable
import mysql.connector
from prettytable import PrettyTable
import tkinter as tk

# Establish a connection to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="code1234",
    database="p5"
)


user_first_name = input("Enter your first name: ")
while True:
    user_passcode = int(input("Enter your passcode: "))
    query = "SELECT * FROM gradebook WHERE first_name = %s AND passcode = %s"
    values = (user_first_name, user_passcode)

    cursor = db_connection.cursor()
    cursor.execute(query, values)

    row = cursor.fetchone()

    if row:
        # Display the data in a table format
        table = PrettyTable(cursor.column_names)
        table.add_row(row)
        print(table)

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()
    else: 
         print("Invalid passcode. Please try again.")

