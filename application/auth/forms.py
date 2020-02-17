from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired(),
        Length(min=1, max=20)])
    password = PasswordField("Password", [DataRequired(),
        Length(min=1, max=20)])
  
    class Meta:
        csrf = False