from flask_mail import Message
from flask import render_template
from . import mail
from .models import User
import time
def mail_message(subject):
    sender_email = 'cephaske254@gmail.com'
    emails = User.query.filter_by(subscribe='true').all()
    for person in emails:
        time.sleep(3)
        email = Message(subject,sender=sender_email,recipients=[person.email])
        email.body = render_template('email/email' + '.txt')
        email.html = render_template('email/email' + '.html')
        mail.send(email)

        time.sleep(3)