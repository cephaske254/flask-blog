from flask import render_template,redirect,request
from . import blog
from .forms import NewPost,TagForm
from ..models import Post,Tag
from app import db,photos
from flask_login import current_user

@blog.route('/')
def index():
    title = 'Blog | TRNB'
    posts = Post.query.all()
    return render_template('blog/index.html',nav=True, title=title,posts=posts)

@blog.route('/new-post',methods=['POST','GET'])
def new_post():
    title = 'New Post | TRNB'
    tags = Tag.get_tags()
    tagform = TagForm()
    form = NewPost()
    if form.is_submitted():
        ptitle = form.title.data
        tag = form.tag.data
        filename = photos.save(request.files['photo'])
        content = form.content.data
        post = Post(title=ptitle,tag=tag,content=content,photo=filename,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
    return render_template('blog/new_post.html',nav=True, title=title,form=form,tagform=tagform,tag_options = tags)

@blog.route('/new_tag',methods=['GET','POST'])
def new_tag():
    if request.environ['HTTP_REFERER'] is not None:
        tagform = TagForm()
        if tagform.is_submitted():
            name = tagform.name.data
            if Tag.query.filter_by(name=name).first() is None:
                tag_ = name.replace(' ', '_')
                tag = Tag(tag=tag_,name=name)
                db.session.add(tag)
                db.session.commit()
        return redirect(request.environ['HTTP_REFERER'])
