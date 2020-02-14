from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(message=None)])
    password = PasswordField("Password", [validators.InputRequired(message=None)])
  
    class Meta:
        csrf = False