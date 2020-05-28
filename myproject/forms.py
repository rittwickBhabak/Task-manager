from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, RadioField, SelectField, PasswordField




# LoginForm, SignUpForm, NewTaskForm, EditTask



class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('LogIn')

class SignUpForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    password = PasswordField('Password')
    confirmPassword = PasswordField('Confirm Password')
    submit = SubmitField('Signup')
