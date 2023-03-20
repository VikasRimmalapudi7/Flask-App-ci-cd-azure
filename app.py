from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Establish a connection to the database
conn = psycopg2.connect(
    host="webappdb.postgres.database.azure.com",
    database="dbname",
    user="server",
    password="Vikas@1379375"
)

# Define a route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the name and age from the form
        name = request.form["name"]
        age = request.form["age"]

        # Create a cursor object for executing SQL queries
        cur = conn.cursor()

        # Execute an INSERT query to add a new row to the table
        cur.execute("INSERT INTO mytable (name, age) VALUES (%s, %s)", (name, age))

        # Commit the changes to the database
        conn.commit()

        # Close the cursor
        cur.close()

        # Render a success message
        return render_template("success.html")

    # Render the home page template
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
