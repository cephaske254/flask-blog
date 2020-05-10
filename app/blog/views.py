from flask import render_template,redirect,request
from . import blog
from .forms import NewPost
from ..models import Post
from app import db,photos
from flask_login import current_user

@blog.route('/')
def index():
    title = 'Blog | TRNB'
    return render_template('blog/index.html',nav=True, title=title)

@blog.route('/new-post',methods=['POST','GET'])
def new_post():
    title = 'New Post | TRNB'
    form = NewPost()
    if form.is_submitted():
        ptitle = form.title.data
        tag = form.tag.data
        filename = photos.save(request.files['photo'])
        content = form.content.data
        post = Post(title=ptitle,tag=tag,content=content,photo=filename,user_id=current_user.id)
        print 
        db.session.add(post)
        db.session.commit()

    return render_template('blog/new_post.html',nav=True, title=title,form=form)

@blog.route('/new_tag',methods=['GET','POST'])
def new_tag():
    if request.environ['HTTP_REFERER'] is not None:
        return redirect(request.environ['HTTP_REFERER'])
