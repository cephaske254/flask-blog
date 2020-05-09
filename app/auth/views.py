from flask import render_template, redirect,url_for
from . import auth
from .forms import SignupForm
from ..models import User,Post
from app import db


@auth.route('/signup', methods =['POST','GET'])
def signup():
    title = 'Signup | TRNB'
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username,password=password,email=email)
        print (user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', title=title, form=form)


@auth.route('/signin')
def signin():
    title = 'Signin | TRNB'
    return render_template('auth/signin.html', title=title)
