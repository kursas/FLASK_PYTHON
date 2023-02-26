from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class ExpensesForm(FlaskForm):
    payment_method = StringField('Atsiskaitymo būdas', [DataRequired()])
    comment = StringField('Komentaras', [DataRequired()])
    amount = FloatField('Suma', [DataRequired()])
    submit = SubmitField('Submit')


class IncomeForm(FlaskForm):
    sender = StringField('Siuntėjas', [DataRequired()])
    comment = StringField('Komentaras', [DataRequired()])
    amount = FloatField('Suma', [DataRequired()])
    submit = SubmitField('Submit')