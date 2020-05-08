from flask import render_template,redirect
from . import auth

@auth.route('/signup')
def signup():
    title = 'Signup | TRNB'
    return render_template('auth/signup.html',title = title)


@auth.route('/signin')
def signin():
    title = 'Signin | TRNB'
    return render_template('auth/signin.html',title = title)