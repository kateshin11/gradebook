from flask import Flask, render_template, request
import mysql.connector
from prettytable import PrettyTable

app = Flask(__name__)

# Establish a connection to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="code1234",
    database="p5"
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_first_name = request.form.get("first_name")
        user_passcode = int(request.form.get("passcode"))
        
        query = "SELECT * FROM gradebook WHERE first_name = %s AND passcode = %s"
        values = (user_first_name, user_passcode)

        cursor = db_connection.cursor()
        cursor.execute(query, values)

        row = cursor.fetchone()

        if row:
            table = PrettyTable(cursor.column_names)
            table.add_row(row)
            result_table = table.get_html_string()
            return render_template("result.html", result_table=result_table)
        else:
            return "Invalid passcode. Please try again."
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
