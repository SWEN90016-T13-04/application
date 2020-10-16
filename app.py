from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import mysql.connector
import os
from forms import CustomerInformationForm

app = Flask(__name__)

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask:password@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Make Db Object
db = SQLAlchemy(app)
# Refelct DB
Base = automap_base()
Base.prepare(db.engine, reflect=True)
#Create Table Model objects
Addresses = Base.classes.addresses
AppointmentBooking = Base.classes.appointment_booking
BeautyCareServices = Base.classes.beauty_care_services
BillerInformation = Base.classes.biller_information
Customers = Base.classes.customers
Users = Base.classes.users


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


#Show all appointments
#TODO: Make accessible to admin only
@app.route('/appointments')
def appointments():
    results = db.session.query(
            AppointmentBooking, Addresses, BeautyCareServices, Customers, Users, 
        ).filter(
            AppointmentBooking.beauty_carer_id == Users.user_id,
        ).filter(
            AppointmentBooking.service_id == BeautyCareServices.service_id,    
        ).filter(
            AppointmentBooking.location == Addresses.address_id,  
        ).filter(
            AppointmentBooking.customer_id == Customers.customer_id  
        ).order_by(AppointmentBooking.date, AppointmentBooking.start_time
        ).all()

    return render_template('appointments.html',
                            title='Booking Registrations',
                            rows=results)



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