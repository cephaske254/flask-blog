from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField,FileField,SelectField
from wtforms.validators import Required
class NewPost(FlaskForm):
    title = StringField('Title',validators=[Required()])
    tag = SelectField('Tag',validators=[Required()])
    content = TextAreaField('Content')
    photo = FileField('Photo', id=None)

class TagForm(FlaskForm):
    name = StringField()
    submit = SubmitField('Add')

class CommentForm(FlaskForm):
    comment = StringField()
    submit = SubmitField('Add')

