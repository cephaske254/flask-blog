from flask import render_template,redirect,request,abort
from . import blog
from .forms import NewPost,TagForm,CommentForm
from ..models import Post,Tag,Comments
from app import db,photos
from flask_login import current_user,login_required

@blog.route('/')
def index():
    title = 'TRN Blog | Home'
    posts = Post.query.all()
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
        post = Post(title=ptitle,tag=tag,content=content,photo=filename,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
    return render_template('blog/new_post.html',nav=True, title=title,form=form,tagform=tagform,tag_options = tags)

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


