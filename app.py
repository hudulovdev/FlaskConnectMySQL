from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'username'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'database_name'  # Replace with your MySQL database name

# Initialize the MySQL extension
mysql = MySQL(app)

@app.route('/')
def home():
    # Example query: fetch all users from the 'users' table
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    
    # Process and display the retrieved data
    user_list = [user[1] for user in users]  # Assuming the name column is at index 1
    return f"Users: {', '.join(user_list)}"

if __name__ == '__main__':
    app.run(debug=True)
