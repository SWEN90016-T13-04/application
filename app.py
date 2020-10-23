from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import mysql.connector
import os
from forms import BookingForm, CustomerInformationForm, EditServices, LoginForm
from flask_login import LoginManager, login_manager, login_required, login_user, current_user, logout_user

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
#Users = Base.classes.users


#Configure Email
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'swen.group1304@gmail.com'
app.config['MAIL_PASSWORD'] = 'swen#swen5916'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)

#User model for authentication
class Users(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    is_beauty_carer = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return Users.query.get(user_id)

# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return 'Hello Boss!  <a href="/logout">Logout</a>'

# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return home()

# @app.route("/logout")
# def logout():
#     session['logged_in'] = False
#     return home()

@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. 
    For POSTS, login the current user by processing the form.

    """
    print(db)
    form = LoginForm()
    if form.validate_on_submit():
        uid = db.session.query(Users).filter(Users.username==form.username.data).one_or_none()
        #TODO return something for invalid user
        user = Users.query.get(uid.user_id)
        if user:
            if user.password == form.password.data:
                print("authenticated")
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect('/')
    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")

#Show all appointments
#TODO: Make accessible to admin only
@app.route('/appointments')
@login_required
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
    
    if not results:
        flash('No Appointments found')
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
def register():
    form = CustomerInformationForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.firstName.data} {form.lastName.data}')
        #Insert for data into database
        # Create Address data object
        reg_address = Addresses(
            unit=form.addressUnit.data,
            building=form.addressBuilding.data,
            street=form.addressStreet.data,
            city=form.addressCity.data,
            state=form.addressState.data,
            country=form.addressCountry.data,
            post_code=form.addressPostCode.data
        )
        db.session.flush()
        db.session.add(reg_address)
        # Create Biller Information data object
        reg_bi = BillerInformation(
            name=form.billerName.data,
            email=form.billerEmail.data
        )
        db.session.add(reg_bi)
        # Flush session so we can access Foreign Keys
        # Create Customer data object
        db.session.flush()
        reg_customer = Customers(
            first_name=form.firstName.data,
            last_name=form.lastName.data,
            phone_number=form.phoneNumber.data,
            email=form.email.data,
            password=form.password.data,
            extra_information=form.extraInformation.data,
            address_id=reg_address.address_id,
            biller_id=reg_bi.biller_id
        )     
        # Commit objects to databse
        db.session.add(reg_customer)
        db.session.commit()
        # Send to some other page
        return redirect('/register')
    return render_template('register.html', 
                            title='Customer Information Form',
                            form=form)

# Edit available Beauty Care Servcies
#TODO implement ability to delete services with QuerySelectField
@app.route('/editservices' , methods=['GET', 'POST'])
@login_required
def edit_servcies():
    form = EditServices()
    if form.validate_on_submit():
        flash(f'Added Service {form.serviceName.data}')
        reg_edit_bcs = BeautyCareServices(
            service_name=form.serviceName.data,
            cost=form.serviceCost.data,
            duration_minutes=form.durationMinutes.data
        )
        db.session.add(reg_edit_bcs)
        db.session.commit()
        return redirect('/editservices')

    return render_template('editservices.html', 
                            title='Edit Beauty Care Services',
                            form=form)



#Book in new appointment

@app.route('/booking', methods=['GET','POST'])
@login_required


"""def service_choices():
    #TODO Check
    return db.session.query(BeautyCareServices.service_name)"""


def booking_appointment():
    form = BookingForm()
    if form.validate_on_submit():
        flash(f'Successfully made booking')
        booking_app = AppointmentBooking(
            date=form.bookingDate.data
            start_time=form.bookingStartTime.data  
            message=form.optionalMessage.data  
        )
        """ Implement columns below to add to database:
        service_id
        location 
        beauty_carer_id=
        customer_id=
        """
        
        db.session.add(booking_app)
        db.session.commit()
        return redirect('/booking')
    
    return render_template('booking.html', 
                            title='Make a Booking',
                            form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
