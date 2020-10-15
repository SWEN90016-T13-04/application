from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class CustomerInformationForm(FlaskForm):
    #Customer information
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    phoneNumber = IntegerField('Phone Number', validators=[DataRequired()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    extraInformation = StringField('Extra Information')
    #Biller information
    billerName = StringField('Name on Invoice')
    billerEmail = EmailField('Biller\'s Email address', [validators.Email()])
    # Address
    addressUnit = StringField('Unit')
    addressBuilding = StringField('Building')
    addressStreet = StringField('Street')
    addressCity = StringField('City / Suburb')
    addressState = StringField('State')
    addressPostCode = StringField('Post Code')
    addressCountry = StringField('Country')
    # Submit
    submit = SubmitField('Submit')