from . import db
from datetime import datetime
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(),unique = True)
    email = db.Column(db.String(),unique = True)
    password = db.Column(db.String())
    bio = db.Column(db.String())
    profile_pic = db.Column(db.String())
    role = db.Column(db.String())
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Post', backref='user',lazy='dynamic')
    

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    publish = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)

