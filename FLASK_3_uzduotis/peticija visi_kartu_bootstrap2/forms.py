from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PetitionForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    surname = StringField('Pavardė', [DataRequired()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Siusti')
