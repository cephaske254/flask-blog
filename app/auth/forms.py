from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Email,Required,EqualTo
from ..models import User

class SignupForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    confirm_password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password',message='Passwords must match!')])
    agree = BooleanField('Agree to T&Cs',validators=[Required()])
    submit = SubmitField('SIGN UP')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered!')
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username Taken!')

class SigninForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    signed_in = BooleanField('Keep me signed in')
    
       