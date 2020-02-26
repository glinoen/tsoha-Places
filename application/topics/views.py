from application import app, db
from flask import render_template, request, redirect, url_for
from application.topics.models import Topic
from application.messages.models import Message
from application.places.models import Place
from datetime import datetime
from application.topics.forms import TopicForm, ReplyForm
from flask_login import login_required, current_user

@app.route("/topics/", methods=["GET"])
@login_required
def topics_index():
    topics = Topic.query.all()
    messages = db.session.query(Message)
    latest_message = Topic.latest()
    filtered_messages = []
    for topic in topics:
        for x in latest_message:
            if x['topic_id'] == topic.id:
                filtered_messages.append(x)
                break
    return render_template("topics/list.html", topics = topics, messages = messages, places = Place.query.all(), latest_message = filtered_messages, datetime = datetime)

@app.route("/topics/new/")
@login_required
def topics_form():
    check = db.session.query(Place).first()
    if check is None:
        firstplace = Place(name = "---", parent_id = None)
        db.session().add(firstplace)
        db.session.commit()
    print("**")
    print("**")
    print(check)
    print("**")
    print("**")
    places = db.session.query(Place)
    form=TopicForm()
    form.place.choices = [(i.id, i.name) for i in places]
       
    return render_template("topics/new.html", form = form)

@app.route("/topics/<topic_id>/", methods=["GET"])
@login_required
def topic_index(topic_id):
    return render_template("topics/topic.html", messages = db.session.query(Message).filter(Message.topic_id == topic_id), topic = Topic.query.get(topic_id), form = ReplyForm())

@app.route("/topics/", methods=["POST"])
@login_required
def topics_create():
    form = TopicForm(request.form)
    if form.title.validate(form) and form.message.validate(form):
        place = db.session.query(Place).get(form.place.data)
        if form.place.data == 0:
            place_id = 0
        else:
            place_id = place.id
          
        topic = Topic(form.title.data, current_user.id, place_id)
        db.session().add(topic)
        db.session().commit()

        message = Message(form.message.data, topic.id, current_user.id)
        db.session().add(message)
        db.session().commit()
    
        return redirect(url_for("topics_index"))
    
    places = db.session.query(Place)
    form=TopicForm()
    form.place.choices = [("0", "---")] + [(i.id, i.name) for i in places]

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