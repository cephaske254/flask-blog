from flask import render_template,redirect,request,abort,url_for
from . import blog
from .forms import NewPost,TagForm,CommentForm
from ..auth import forms as auth_forms
from ..models import Post,Tag,Comments,User
from app import db,photos
from flask_login import current_user,login_required
import os
from config import Config
from ..email import mail_message

uploaded_photos = Config.UPLOADED_PHOTOS_DEST
@blog.route('/')
def index():
    title = 'TRN Blog | Home'
    posts = Post.get_all()
    return render_template('blog/index.html',nav=True, title=title,posts=posts)

@blog.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post.get_single_post(post_id)
    title =f'TRN Blog | {post.title}'
    comments = Comments.get_comments(post_id)
    form = CommentForm()
    if post_id is None or post is None:
        abort(404)
    return render_template('blog/single_post.html', title=title,post=post,form=form,nav=True, comments=comments)

@blog.route('/new-post',methods=['POST','GET'])
@login_required
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
        post = Post(title=ptitle,tag_id=tag,content=content,photo=filename,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        mail_message('New Blog Post!')

        return redirect(url_for('blog.index'))
    return render_template('blog/new_post.html',nav=True, title=title,form=form,tagform=tagform,tag_options = tags)
    # os.remove(os.path.join(app.config['UPLOADED_ITEMS_DEST'], item.filename))

@blog.route('/edit-post/<int:post_id>',methods=['POST','GET'])
@login_required
def edit_post(post_id):
    tagform = TagForm()
    form = NewPost()
    tags = Tag.get_tags()
    post = Post.get_single_post(post_id)
    title = f'Edit {post.title} | TRNB'
    if form.is_submitted():
        post.title = form.title.data
        post.tag = form.tag.data
        post.content = form.content.data
        if form.photo.data:
            os.remove(os.path.join(uploaded_photos,post.photo))
            filename = photos.save(request.files['photo'])
            post.photo = filename

        db.session.commit()
        return redirect(url_for('.single_post', post_id=post_id))

    return render_template('blog/edit_post.html',nav=True, title=title,form=form,tagform=tagform,tag_options = tags, post=post)

@blog.route('/post/<int:post_id>/delete',methods=['POST','GET'])
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect (url_for('blog.index'))

@blog.route('/new_tag',methods=['GET','POST'])
@login_required
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

@blog.route('/comment/<int:post_id>',methods=['GET','POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    if form.is_submitted():
        comment = Comments(user_id = current_user.id, post_id=post_id,comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(request.environ['HTTP_REFERER'])

@blog.route('/comment/<int:comment_id>/delete',methods=['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment = Comments.query.filter_by(id=comment_id)
    comment.delete()
    db.session.commit()

    return redirect(request.environ['HTTP_REFERER'])

@blog.route('/subscribe',methods=['GET','POST'])
@login_required
def subscribe():
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if user.subscribe == 'true':
            state = user.subscribe='false'
        else:
            state = user.subscribe='true'

        db.session.add(user)
        db.session.commit()

    return redirect(url_for(request.environ['HTTP_REFERER']))


