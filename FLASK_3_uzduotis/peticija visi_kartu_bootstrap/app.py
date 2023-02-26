from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from forms import PetitionForm
from datetime import datetime


TOTAL_SIGNATURES = 10000

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


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))

    def __init__(self, name, surname, comment):
        self.name = name
        self.surname = surname
        self.comment = comment

    def __repr__(self):
        return f'{self.name} - {self.surname} - {self.date} - {self.comment}'


@application.route('/', methods=['GET', 'POST'])
def index():
    form = PetitionForm()
    if form.validate_on_submit():
        # Take data from the (now validated) form
        fname = form.name.data
        sname = form.surname.data
        comment = form.comment.data
        # Create instance of Person class / entry in DB
        # Represents data of a person who has signed the petition
        entry = Person(name=fname, surname=sname, comment=comment)
        # Add and commit to the database
        db.session.add(entry)
        db.session.commit()
        # Query all person data and reverse order (we want to show up-to-date information)
        data = Person.query.all()[::-1]
        # Compute how many signatures are remaining
        # (note that if we have over TOTAL_SIGNATURES in the database, we will get minus numbers because
        # we haven't done anything about that. Exercise: change it so that we have a different page once
        # this is filled)
        remaining = TOTAL_SIGNATURES - len(data)
        return render_template('index_success.html', signee_name=fname, data=data, remaining=remaining)
    # Query all person data and reverse order
    data = Person.query.all()[::-1]
    return render_template('index.html', form=form, data=data)


@application.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    db.create_all()
    application.run(host='127.0.0.1', port=8000, debug=True)
