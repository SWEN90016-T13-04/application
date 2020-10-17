from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, SubmitField, IntegerField, DecimalField
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

class EditServices(FlaskForm):
    #Add a servcies
    serviceName = StringField('Service Name', validators=[DataRequired()])
    serviceCost = DecimalField('Service Cost', places=2, rounding=ROUND_HALF_UP, validators=[DataRequired()])
    durationMinutes = IntegerField('Duration Minutes', validators=[DataRequired()])
    #Submit Form
    submit = SubmitField('Submit')