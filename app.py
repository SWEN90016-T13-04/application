from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
import mysql.connector
import os
from forms import CustomerInformationForm

app = Flask(__name__)

# Create database connection
config = {
    'user': 'flask',
    'password': 'password',
    'host': 'localhost',
    'port': '3306',
    'database': 'mydb'
}
connection = mysql.connector.connect(**config)

#Configure Email
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'swen.group1304@gmail.com'
app.config['MAIL_PASSWORD'] = 'swen#swen5916'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


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

# test endpoint for database
@app.route("/dbtest")
def dbtest():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM addresses;')
    results = cursor.fetchall()
    return results[0]

#basic endpoint to send
@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'swen.group1304@gmail.com', recipients = ['samtpjones@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@app.route('/register' , methods=['GET', 'POST'])
def login():
    form = CustomerInformationForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.firstName.data} {form.lastName.data}')
        return redirect('/')
    return render_template('register.html', title='Customer Information Form', form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)