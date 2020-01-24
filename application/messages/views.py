from application import app
from flask import request, redirect, url_for
from application.messages.models import Message

@app.route("/topics/<topic_id>/", methods=["POST"])
def messages_create(topic_id):
    m = Message(request.form.get("content"))
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("topic_index"))