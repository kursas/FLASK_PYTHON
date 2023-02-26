from flask import Flask, render_template, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from forms import ExpensesForm, IncomeForm
from datetime import datetime


# Create Flask app
application = Flask(__name__)
application.config['SECRET_KEY'] = '123asd123'
# Make context available to all files
application.app_context().push()

# Path to our current directory (useful for creating databases in the same directory)
basedir = os.path.abspath(os.path.dirname(__file__))
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# Don't track modifications
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)


class Expenses(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))

    def __init__(self, payment_method, comment, amount):
        self.payment_method = payment_method
        self.comment = comment
        self.amount = amount

    def __repr__(self):
        return f'{self.payment_method} - {self.comment} - {self.amount}'


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))

    def __init__(self, sender, comment, amount):
        self.sender = sender
        self.comment = comment
        self.amount = amount

    def __repr__(self):
        return f'{self.sender} - {self.comment} - {self.amount}'


@application.route('/')
def index():
    income_data = Income.query.all()
    expenses_data = Expenses.query.all()
    income_sum = sum([entry.amount for entry in income_data])
    expenses_sum = sum([entry.amount for entry in expenses_data])
    balance = income_sum - expenses_sum
    return render_template('index.html', balance=balance, income_data=income_data, expenses_data=expenses_data)


@application.route('/income', methods=['GET', 'POST'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        # Take data from the (now validated) form
        sender = form.sender.data
        comment = form.comment.data
        amount = form.amount.data
        # Create instance of Income class / entry in DB
        entry = Income(sender=sender, comment=comment, amount=amount)
        # Add and commit to the database
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('income.html', form=form)


@application.route('/expenses', methods=['GET', 'POST'])
def expenses():
    form = ExpensesForm()
    if form.validate_on_submit():
        # Take data from the (now validated) form
        payment_method = form.payment_method.data
        comment = form.comment.data
        amount = form.amount.data
        # Create instance of Income class / entry in DB
        entry = Expenses(payment_method=payment_method, comment=comment, amount=amount)
        # Add and commit to the database
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('expenses.html', form=form)


if __name__ == '__main__':
    db.create_all()
    application.run(host='127.0.0.1', port=8000, debug=True)
