from . import db,login_manager
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(id):
    return User.query.get(id)

def get_by_mail_username(username_mail):
    user = User.query.filter_by(username = username_mail).first()
    if user is None:
        user = User.query.filter_by(email=username_mail).first()
    return user
    
class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(),unique = True)
    email = db.Column(db.String(),unique = True)
    password_hash = db.Column(db.String())
    bio = db.Column(db.String())
    profile_pic = db.Column(db.String())
    role = db.Column(db.String(),default='user')
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Post', backref='user',lazy='dynamic')
    Comments = db.relationship('Comments', backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password_raw):
        self.password_hash = generate_password_hash(password_raw)

    def verify_password(self, password_raw):
        return check_password_hash(self.password_hash, password_raw)

    @classmethod
    def get_user(cls,id):
        return User.query.get(id)

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    publish = db.Column(db.String(),default=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    photo = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    tag_name = db.relationship('Tag', backref='tag_name')
    reactions = db.relationship('Reactions',backref='reaction')


class Tag(db.Model):
    __tablename__='tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    tag = db.Column(db.String())

    @classmethod
    def get_tags(cls):
        return Tag.query.all()

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.String())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
