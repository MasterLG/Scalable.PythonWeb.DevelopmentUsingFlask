from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError

from user.models import User


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

    def validate_username(form, field):  # custom validator
        if User.objects.filter(username=field.data).first():
            raise ValidationError('Username already exists.')

    def validate_email(form, field):
        if User.objects.filter(email=field.data).first():
            raise ValidationError("Email already in use.")

class LoginForm(Form):
    username = StringField(
        'Username', [validators.DataRequired(), validators.length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired(),  validators.length(min=4, max=80)])