from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, DateField, PasswordField, BooleanField, TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RecordForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    phone = StringField('Phone:', validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    address = StringField("Address: ", validators = [])
    birthday = StringField("Birthday", validators=[DataRequired()])
    submit = SubmitField('OK')