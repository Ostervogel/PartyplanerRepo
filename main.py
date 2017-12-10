from flask_bootstrap import Bootstrap
from flask import Flask, session, render_template, request, redirect, g, url_for
import os
import json
from pprint import pprint

# Instanz von Flask
app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.urandom(24)
pw = ""
with open('secrets/conf.json') as data_file:
    data = json.load(data_file)
    for x in data.values():
        pw = x


# Routet zur Default Page
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == pw:
            session['user'] = request.form['username']
            return redirect(url_for('startseite'))

    return render_template('login.html')


@app.route('/startseite')
def startseite():
    if g.user:
        return render_template('index.html')

    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Nicht eingeloggt!'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'


# _name_ wird automatisch zu main wenn das Programm gestartet wird
if __name__ == "__main__":
    app.run(debug=True)
