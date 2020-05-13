from flask import render_template,redirect
from . import main

@main.route('/welcome')
def welcome():
    return render_template('welcome.html',title='Home')
    
from . import errors
