from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.validators import DataRequired, Length, InputRequired
from application.places.models import Place


class PlaceForm(FlaskForm):

    title = StringField("Name", [DataRequired(), Length(min=1, max=20)])

    parentplace = SelectField(u'New place exists inside', coerce=int, validators=[InputRequired()])


    class Meta:
        csrf = False