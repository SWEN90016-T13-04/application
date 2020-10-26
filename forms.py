from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, SubmitField, IntegerField, DecimalField, SelectField, DateTimeField, DateField, TimeField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from decimal import ROUND_HALF_UP
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import mysql.connector



class CustomerInformationForm(FlaskForm):
    #Customer information
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    phoneNumber = IntegerField('Phone Number', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    extraInformation = StringField('Extra Information')
    #Biller information
    billerName = StringField('Name on Invoice' , validators=[DataRequired()])
    billerEmail = EmailField('Biller\'s Email address', validators=[DataRequired(), Email()])
    # Address
    addressUnit = StringField('Unit')
    addressBuilding = StringField('Building')
    addressStreet = StringField('Street', validators=[DataRequired()])
    addressCity = StringField('City / Suburb', validators=[DataRequired()])
    addressState = StringField('State', validators=[DataRequired()])
    addressPostCode = StringField('Post Code', validators=[DataRequired()])
    addressCountry = StringField('Country', validators=[DataRequired()])
    # Submit Form
    submit = SubmitField('Submit')

class CustomerProfile(CustomerInformationForm):
    #Customer information
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    phoneNumber = StringField('Phone Number')
    email = EmailField('Email address')
    password = PasswordField('Password')
    extraInformation = StringField('Extra Information')
    #Biller information
    billerName = StringField('Name on Invoice')
    billerEmail = EmailField('Biller\'s Email address')
    # Address
    addressUnit = StringField('Unit')
    addressBuilding = StringField('Building')
    addressStreet = StringField('Street')
    addressCity = StringField('City / Suburb')
    addressState = StringField('State')
    addressPostCode = StringField('Post Code')
    addressCountry = StringField('Country')
    # Submit Form
    submit = SubmitField('Update')

class EditServices(FlaskForm):
    #Add a servcies
    # serviceName = StringField('Service Name', validators=[DataRequired()])
    serviceName = SelectField('Service Name', choices=['haircut', 'hair wash & dry', 'hair colour'])
    serviceCost = DecimalField('Service Cost', places=2, rounding=ROUND_HALF_UP, validators=[DataRequired()])
    # appointmentTime = DateTimeField('Time of the appointment', format='%d-%m-%Y %H:%M:%S')
    #optional message
    bookingMessage = StringField('Optional Message')
    #Submit Form
    submit = SubmitField('Submit')

class BookingForm(FlaskForm):
    #Add a servcies
    bookingName = SelectField('Service Name', choices=['haircut', 'hair wash & dry', 'hair colour'], validators=[DataRequired()])
    # serviceCost = DecimalField('Service Cost', places=2, rounding=ROUND_HALF_UP, validators=[DataRequired()])
    bookingDate = DateField('Date of the appointment YYYY-MM-DD', validators=[DataRequired()])
    #Submit Form
    submit = SubmitField('Check Date Availability')

class AvailabilityForm(FlaskForm):
    availabilityTime = SelectField('Start times:', coerce=str, validators=[DataRequired()])
    availabilityServices = SelectField('Service Cost:', coerce=float, validators=[DataRequired()])
    availabilityLocation = StringField('Location (leave empty to use Customer Address):')
    availabilityMessage = StringField('Optional Message for the carer:')
    submit = SubmitField('Book')

class LoginForm(FlaskForm):
    username = EmailField('Username / Email')
    password = PasswordField('Password')
    submit = SubmitField('Submit')