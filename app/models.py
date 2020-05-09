from . import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(),unique = True)
    email = db.Column(db.String(),unique = True)
    password = db.Column(db.String())
    bio = db.Column(db.String())
    profile_pic = db.Column(db.String())