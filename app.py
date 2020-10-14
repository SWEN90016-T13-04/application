from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import mysql.connector
import os

app = Flask(__name__)



# Create connection
config = {
    'user': 'flask',
    'password': 'password',
    # "host": "db",
    'host': 'localhost',
    'port': '3306',
    'database': 'mydb'
}
connection = mysql.connector.connect(**config)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Hello Boss!  <a href="/logout">Logout</a>'

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/dbtest")
def dbtest():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM addresses;')
    results = cursor.fetchall()
    return results[0]

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)