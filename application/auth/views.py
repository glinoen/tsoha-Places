from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate_on_submit():
        return render_template("auth/loginform.html", form = form,
                               error = "username and password must be between 1-20 characters")
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("topics_index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("topics_index")) 

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = LoginForm())
    
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
    
        db.session().add(user)
        db.session.commit()
        return redirect(url_for("auth_login"))
    
    return render_template("auth/registerform.html", form=form,  error = "username and password must be between 1-20 characters")

    

    