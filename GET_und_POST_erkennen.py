from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Method used: %s" % request.method


@app.route("/bacon", methods=["GET", "POST"])  # Diese Seite kann GET und POST requests abarbeiten.
def bacon():
    if request.method == "POST":
        return "You are using POST"
    else:
        return "You are probably using GET"

# if __name__ == "__main__":
#   app.run(debug=True)
