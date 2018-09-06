from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError


class RegisterForm(Form):
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email Address', [
                       validators.DataRequired(), validators.Email()])
    username = StringField(
        'Username', [validators.DataRequired(), validators.length(min=4, max=25)])
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo(
        'confirm', message='Passwords must match'), validators.length(min=4, max=80)])
    confirm = PasswordField('Repeat Password')
