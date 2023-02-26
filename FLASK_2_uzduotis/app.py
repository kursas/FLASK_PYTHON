from flask import Flask, render_template, request, redirect, url_for, flash
from form import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdf10#$'

@app.route('/', methods=['GET', 'POST'])
def form():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('success.html', form=form)
    return render_template('form.html', form=form)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
  
 #output
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 562-961-431
127.0.0.1 - - [26/Feb/2023 20:34:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/Feb/2023 20:34:06] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [26/Feb/2023 20:34:35] "POST / HTTP/1.1" 200 -

Process finished with exit code 0
