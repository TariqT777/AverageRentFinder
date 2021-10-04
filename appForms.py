from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class cityStateForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Find Avg')