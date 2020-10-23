from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import mysql.connector
import os
from forms import CustomerInformationForm, EditServices, LoginForm, CustomerProfile
from flask_login import LoginManager, login_manager, login_required, login_user, current_user, logout_user

app = Flask(__name__)

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask:password@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Make Db Object
db = SQLAlchemy(app)
# Reflect DB
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
    username =  db.Column(db.String)
    password = db.Column(db.String)
    privileges = db.Column(db.Integer, default=0)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    customer_id = db.Column(db.Integer)
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

    def get_username(self):
        """Returns username."""
        return self.username

    def get_privileges(self):
        """Returns user privileges"""
        return self.privileges

    def get_attribute(self, attribute_name):
        """Returns any attribute by name, except password"""
        if attribute_name != 'password':
            return getattr(self, attribute_name)

def get_customer_details(customer_id):
    """Get a customers details based on its ID"""
    details = {
        'phone_number':'Not set',
        'address_id':'Not set',
        'extra_information':'Not set',
        'biller_id':'Not set'
    }

    if customer_id:
        customer = db.session.query(Customers).filter_by(customer_id=customer_id).first()
        details = {
            'phone_number':customer.phone_number,
            'address_id':customer.address_id,
            'extra_information':customer.extra_information,
            'biller_id':customer.biller_id
        }

    return details

def get_customer_biller_info(biller_id):
    """Get a customer's biller information based on its biller ID"""
    details = {
        'name':'Not set',
        'email':'Not set'
    }

    if biller_id != 'Not set':
        customer = db.session.query(BillerInformation).filter_by(biller_id=biller_id).first()
        try:
            details = {
                'name':customer.name if customer.name else 'Not set',
                'email':customer.email if customer.email else 'Not set',
            }
        except:
            return details
    return details

def get_customer_address(address_id):
    """Get a customer's  address based on its address ID"""
    details = {
        'unit':'Not set',
        'building':'Not set',
        'street':'Not set',
        'city':'Not set',
        'state':'Not set',
        'country':'Not set',
        'post_code':'Not set'
    }

    if address_id != 'Not set':
        customer = db.session.query(Addresses).filter_by(address_id=address_id).first()
        details = {
            'unit': customer.unit if customer.unit else 'Not set',
            'building': customer.building if customer.building else 'Not set',
            'street': customer.street if customer.street else 'Not set',
            'city': customer.city if customer.city else 'Not set',
            'state': customer.state if customer.state else 'Not set',
            'country': customer.country if customer.country else 'Not set',
            'post_code': customer.post_code if customer.post_code else 'Not set',
        }

    return details

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
        try:
            user = Users.query.get(uid.user_id)
            if user:
                if user.password == form.password.data:
                    print("authenticated")
                    user.authenticated = True
                    db.session.add(user)
                    db.session.commit()
                    login_user(user, remember=True)
                    return redirect('/')
        except:
            return render_template("login.html", form=form)
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
   msg = Message('Hello', sender = 'swen.group1304@gmail.com', recipients = ['jbarriossute@student.unimelb.edu.au'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = CustomerProfile()
    user = current_user
    details = get_customer_details(user.get_attribute('customer_id'))
    biller_info = get_customer_biller_info(details['biller_id'])
    address_info = get_customer_address(details['address_id'])

    if form.validate_on_submit():
        try:
            breakpoint()
            change = False
            customer = db.session.query(Addresses).filter_by(address_id=details['address_id']).first()
            if form.addressUnit.data != '':
                customer.unit = form.addressUnit.data
                change = True
            if form.addressCity.data != '':
                customer.city = form.addressCity.data
                change = True
            if form.addressStreet.data != '':
                customer.street = form.addressStreet.data
                change = True
            if form.addressState.data != '':
                customer.state = form.addressState.data
                change = True
            if form.addressPostCode.data != '':
                customer.post_code = form.addressPostCode.data
                change = True
            if form.addressCountry.data != '':
                customer.country = form.addressCountry.data
                change = True

            customer = db.session.query(BillerInformation).filter_by(biller_id=details['biller_id']).first()
            if form.billerName.data != '':
                customer.name = form.billerName.data
                change = True
            if form.billerEmail.data != '':
                customer.email = form.billerEmail.data
                change = True

            customer = db.session.query(Customers).filter_by(customer_id=user.get_attribute('customer_id')).first()
            if form.phoneNumber.data != '':
                customer.phone_number = form.phoneNumber.data
                change = True
            if form.extraInformation.data != '':
                customer.extra_information = form.extraInformation.data
                change = True
            if form.firstName.data != '':
                user.first_name = form.firstName.data
                change = True

            if change:
                db.session.commit()
                flash(f'Profile data updated')

                details = get_customer_details(user.get_attribute('customer_id'))
                biller_info = get_customer_biller_info(details['biller_id'])
                address_info = get_customer_address(details['address_id'])

        except:
            flash(f'Profile could not be updated succesfully')

    return render_template('profile.html',
                                title='Customer Profile Information',
                                form=form,
                                details=details,
                                biller_info=biller_info,
                                address_info=address_info)

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
            phone_number=form.phoneNumber.data,
            address_id=reg_address.address_id,
            extra_information=form.extraInformation.data,
            biller_id=reg_bi.biller_id
        )

        # Commit objects to databse
        db.session.add(reg_customer)
        db.session.flush()
        # Send to some other page

        # (`user_id`, `username`, `password`, `privileges`, `first_name`, `last_name`, `customer_id`, `authenticated`)
        reg_user = Users(
            username=form.email.data,
            password=form.password.data,
            privileges=1,
            first_name=form.firstName.data,
            last_name=form.lastName.data,
            customer_id=reg_customer.customer_id,
            authenticated=0,
        )
        db.session.add(reg_user)
        db.session.commit()

        return redirect('/register')
    return render_template('register.html', 
                            title='Customer Information Form',
                            form=form)

# TODO: Changes don't seem to be persistent?

# Edit available Beauty Care Services
#TODO implement ability to delete services with QuerySelectField
@app.route('/editservices' , methods=['GET', 'POST'])
@login_required
def edit_services():
    if current_user.get_privileges() >= 7:
        form = EditServices()
        if form.validate_on_submit():
            flash(f'Added Service {form.serviceName.data}')
            reg_edit_bcs = BeautyCareServices(
                service_name=form.serviceName.data,
                cost=form.serviceCost.data,
                # duration_minutes=form.durationMinutes.data
            )
            db.session.add(reg_edit_bcs)
            db.session.commit()
            return redirect('/editservices')

        return render_template('editservices.html',
                                title='Edit Beauty Care Services',
                                form=form)
    else:
        return redirect('/')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)