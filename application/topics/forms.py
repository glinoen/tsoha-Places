from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TopicForm(FlaskForm):
    title = StringField("Topic title", [validators.InputRequired(message=None)])
    message = StringField("Message", [validators.InputRequired(message=None)])

    class Meta:
        csrf = False

class ReplyForm(FlaskForm):
    reply = StringField("Reply", [validators.InputRequired(message=None)])

    class Meta:
        csrf = False