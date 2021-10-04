from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class cityStateForm(FlaskForm):
    city = StringField('City', validators=[InputRequired()])
    state = StringField('State', validators=[InputRequired()])
    submit = SubmitField('Find Avg')