from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Email,Required,EqualTo

class SignupForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    confirm_password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password',message='Passwords must match!')])
    confirm_password = BooleanField('Agree to T&Cs',validators=[Required()])
    submit = SubmitField('SIGN UP')