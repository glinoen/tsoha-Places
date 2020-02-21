from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


# tietokanta
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///topics.db"    
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

# Luetaan sovelluksen toiminnallisuudet
from application import views
from application import places

from application.topics import models
from application.topics import views

from application.auth import models
from application.auth import views

from application.places import models
from application.places import views

#kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut

try:
    db.create_all()
except:
    pass