from flask import render_template,redirect,request
from . import blog

@blog.route('/')
def index():
    title = 'Blog | TRNB'
    return render_template('blog/index.html',nav=True, title=title)

@blog.route('/new-post')
def new_post():
    title = 'New Post | TRNB'
    return render_template('blog/new_post.html',nav=True, title=title)

@blog.route('/new_tag',methods=['GET','POST'])
def new_tag():
    if request.environ['HTTP_REFERER'] is not None:
        return redirect(request.environ['HTTP_REFERER'])
