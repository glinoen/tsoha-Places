from application import app, db
from flask import render_template, request, redirect, url_for
from application.topics.models import Topic
from application.messages.models import Message
from application.places.models import Place
from application.places.forms import PlaceForm
from flask_login import login_required, current_user

@app.route("/newplace/", methods=["GET"])
@login_required
def place_form():
    places = db.session.query(Place)
    form=PlaceForm()
    form.parentplace.choices = [("0", "---")] + [(i.id, i.name) for i in places]

    return render_template("places/newplace.html", form = form)

@app.route("/newplace", methods=["POST"])
@login_required
def place_create():
    form = PlaceForm(request.form)
    if form.title.validate(form):
    
        parent = db.session.query(Place).get(form.parentplace.data)
        if parent is None:
            parent_id = 0
        else:
            parent_id = parent.id

        place = Place(form.title.data, parent_id)
        db.session().add(place)
        db.session().commit()

        return redirect(url_for("topics_form"))
    
    places = db.session.query(Place)
    form=PlaceForm()
    form.parentplace.choices = [("0", "---")] + [(i.id, i.name) for i in places]

    return render_template("places/newplace.html", form = form, error="place name must be between 1-20 characters")

