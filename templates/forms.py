from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = StringField('Sign up')