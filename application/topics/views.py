from application import app, db
from flask import render_template, request, redirect, url_for
from application.topics.models import Topic
from application.messages.models import Message
from application.topics.forms import TopicForm, ReplyForm
from flask_login import login_required, current_user

@app.route("/topics/", methods=["GET"])
@login_required
def topics_index():
    messages = db.session.query(Message)
    return render_template("topics/list.html", topics = Topic.query.all(), messages = messages)

@app.route("/topics/new/")
@login_required
def topics_form():
    return render_template("topics/new.html", form = TopicForm())

@app.route("/topics/<topic_id>/", methods=["GET"])
@login_required
def topic_index(topic_id):
    return render_template("topics/topic.html", messages = db.session.query(Message).filter(Message.topic_id == topic_id), topic = Topic.query.get(topic_id), form = ReplyForm())

@app.route("/topics/", methods=["POST"])
@login_required
def topics_create():
    form = TopicForm(request.form)
    if form.validate_on_submit():        
        topic = Topic(form.title.data, current_user.id)
        db.session().add(topic)
        db.session().commit()

        message = Message(form.message.data, topic.id, current_user.id)
        db.session().add(message)
        db.session().commit()
    
        return redirect(url_for("topics_index"))
    
    return render_template("topics/new.html", form = form, error="topic name must be between 1-100 characters and message between 1-1000 characters")
    

@app.route("/topics/<topic_id>/", methods=["POST"])
@login_required
def messages_create(topic_id):
    form = ReplyForm(request.form)
    if form.validate_on_submit():
        message = Message(form.reply.data, topic_id, current_user.id)
        
        db.session().add(message)
        db.session().commit()
    
        return redirect(url_for("topic_index", topic_id = topic_id))
    
    return render_template("topics/topic.html", messages = db.session.query(Message).filter(Message.topic_id == topic_id), topic = Topic.query.get(topic_id), form = form, error="message must be between 1-1000 characters")


@app.route('/delete/<message_id>', methods=['POST'])
@login_required
def messages_delete(message_id):
    message = Message.query.filter_by(id=message_id).first()
    topic_id = message.topic_id
    print("************************************")
    print(message)
    db.session().delete(message)
    db.session().commit()
  
    return redirect(url_for("topic_index", topic_id = topic_id))