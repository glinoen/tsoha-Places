from application import app, db
from flask import render_template, request, redirect, url_for
from application.topics.models import Topic, Message

@app.route("/topics/", methods=["GET"])
def topics_index():
    messages = db.session.query(Message)
    return render_template("topics/list.html", topics = Topic.query.all(), messages = messages)

@app.route("/topics/new/")
def topics_form():
    return render_template("topics/new.html")

@app.route("/topics/<topic_id>/", methods=["GET"])
def topic_index(topic_id):
    return render_template("topics/topic.html", messages = db.session.query(Message).filter(Message.topic_id == topic_id), topic = Topic.query.get(topic_id))

@app.route("/topics/", methods=["POST"])
def topics_create():
    name = request.form.get("name")
    t = Topic(name)
    db.session().add(t)
    db.session().commit()

    m = Message(request.form.get("message"), t.id)
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("topics_index"))


@app.route("/topics/<topic_id>/", methods=["POST"])
def messages_create(topic_id):
    m = Message(request.form.get("name"), topic_id)
    
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("topic_index", topic_id = topic_id))