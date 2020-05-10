from flask import render_template, redirect,url_for,flash,request
from . import auth
from .forms import SignupForm,SigninForm
from ..models import User,Post,get_by_mail_username
from app import db
from flask_login import login_user


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
        return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', title=title, form=form)


@auth.route('/signin',methods=['GET','POST'])
def signin():
    title = 'Signin | TRNB'
    form = SigninForm()
    if form.is_submitted():
        username = form.username.data
        password = form.password.data
        signed_in = form.signed_in.data
        user = get_by_mail_username(username)
        if user is not None and user.verify_password(form.password.data):
            login_user(user,signed_in)
            return redirect(request.args.get('next') or url_for('blog.index'))
        flash('Wrong credentials!')
    return render_template('auth/signin.html', title=title,form=form)
