from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Length

class TopicForm(FlaskForm):
    title = StringField("Topic title", [DataRequired(),
        Length(min=1, max=100)])
    message = StringField("Message", [DataRequired(),
        Length(min=1, max=1000)])

    class Meta:
        csrf = False

class ReplyForm(FlaskForm):
    reply = StringField("Reply", [DataRequired(),
        Length(min=1, max=1000)])

    class Meta:
        csrf = False