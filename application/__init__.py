from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

# Käytetään topics.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///topics.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import places

from application.topics import models

from application.topics import views

##from application.messages import models

##from application.messages import views



# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()