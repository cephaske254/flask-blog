from flask import render_template,redirect
from . import blog

@blog.route('/')
def index():
    title = 'Blog | TRNB'
    return render_template('blog/index.html',nav=True, title=title)