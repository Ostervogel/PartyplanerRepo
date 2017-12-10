from flask import Flask, request

app = Flask(__name__)  # Schreibt das Flaskobjekt in die Variable app. Mit dem Parameter __name__.


@app.route("/")  # Die Variable ruft route() auf. Im Parameter steht die URL die aufgerufen werden muss.
def index():  # Schreibt die Methode die auf der Seite aufgerufen werden soll.
    return "Method used: %s" % request.method  # Sagt ob GET oder POST benutzt wurde.


@app.route("/tuna")
def tuna():
    return "<h2>Tuna is good<h2>"  # Gibt Text aus


@app.route("/profile/<int:post_id>")  # Gibt das in der URL geschriebene auf der Website aus-
def show_post(post_id):
    return "<h2>Post ID is %s<h2>" % post_id
