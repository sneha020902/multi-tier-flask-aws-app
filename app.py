from flask import Flask, render_template, request, redirect, url_for
import pymysql
from config import db_config  # Separate config file

app = Flask(__name__)

# Function to get DB connection
'''
here's what I used 
db_config = {
    'host': 'sneha-db.cl0m8aa8o62s.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'password54321',
    'database': 'sneha_db'
}
'''
def get_connection():
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

@app.route('/')
def home():
    return redirect(url_for('add_user'))

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_users'))

    return render_template('form.html')

@app.route('/users')
def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
