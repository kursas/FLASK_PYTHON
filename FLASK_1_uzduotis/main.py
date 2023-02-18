#Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu (rekomenduojama naudoti šablonus)
#Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio) ir paspaudus ENTER, atspausdintų jį penkis kartus.
#Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.
#Sukurti programą, kuri leistų įvesti metus ir paspaudus patvirtinimo mygtuką parodytų, ar jie yra keliamieji.
from flask import Flask, render_template, request
from calendar import isleap
import datetime

app = Flask(__name__)

@app.context_processor
def add_imports():
    masyvas = {"isleap": isleap,
               "datetime": datetime}
    return masyvas

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/address/<vardas>")
def address(vardas):
    return render_template('address.html', vardas=vardas)

@app.route("/keliamieji")
def keliamieji():
    # masyvas = [metai for metai in range(1900, 2100) if isleap(metai)]
    # return render_template('keliamieji.html', metai=masyvas)
    return render_template('keliamieji.html')


@app.route("/ar_keliamieji", methods=['GET', 'POST'])
def ar_keliamieji():
    metai = False
    if request.method == "POST":
        metai = int(request.form['metai'])
    return render_template('ar_keliamieji.html', metai=metai)

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
