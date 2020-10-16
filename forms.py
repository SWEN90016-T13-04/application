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
    billerName = StringField('Name on Invoice' , validators=[DataRequired()])
    billerEmail = EmailField('Biller\'s Email address', [validators.DataRequired(), validators.Email()])
    # Address
    addressUnit = StringField('Unit')
    addressBuilding = StringField('Building')
    addressStreet = StringField('Street', validators=[DataRequired()])
    addressCity = StringField('City / Suburb', validators=[DataRequired()])
    addressState = StringField('State', validators=[DataRequired()])
    addressPostCode = StringField('Post Code', validators=[DataRequired()])
    addressCountry = StringField('Country', validators=[DataRequired()])
    # Submit
    submit = SubmitField('Submit')