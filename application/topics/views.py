from application import app, db
from flask import render_template, request, redirect, url_for
from application.topics.models import Topic, Message
from application.topics.forms import TopicForm, ReplyForm

@app.route("/topics/", methods=["GET"])
def topics_index():
    messages = db.session.query(Message)
    return render_template("topics/list.html", topics = Topic.query.all(), messages = messages)

@app.route("/topics/new/")
def topics_form():
    return render_template("topics/new.html", form = TopicForm())

@app.route("/topics/<topic_id>/", methods=["GET"])
def topic_index(topic_id):
    return render_template("topics/topic.html", messages = db.session.query(Message).filter(Message.topic_id == topic_id), topic = Topic.query.get(topic_id), form = ReplyForm())

@app.route("/topics/", methods=["POST"])
def topics_create():
    form = TopicForm(request.form)
    t = Topic(form.title.data)
    db.session().add(t)
    db.session().commit()

    m = Message(form.message.data, t.id)
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("topics_index"))


@app.route("/topics/<topic_id>/", methods=["POST"])
def messages_create(topic_id):
    form = ReplyForm(request.form)
    m = Message(form.reply.data, topic_id)
    
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("topic_index", topic_id = topic_id))