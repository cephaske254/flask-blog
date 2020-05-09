from . import db
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(),unique = True)
    email = db.Column(db.String(),unique = True)
    password = db.Column(db.String())
    bio = db.Column(db.String())
    profile_pic = db.Column(db.String())
    role = db.Column(db.String(),default='user')
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Post', backref='user',lazy='dynamic')

    @property
    def password_raw(self):
        raise AttributeError('You cannnot read the password attribute')

    @password_raw.setter
    def password(self, password_raw):
        self.password_hash = generate_password_hash(password_raw)

    def verify_password(self, password_raw):
        return check_password_hash(self.password, password_raw)

    @classmethod
    def get_user(cls,id):
        return User.query.get(id)

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    publish = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)

