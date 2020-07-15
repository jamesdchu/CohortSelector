# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=["GET","POST"])
def results():
    if request.method == "POST":
        props = {
            "food":request.form["food"],
            "nickname":request.form["nickname"],
            "color":request.form["color"],
            "birthmonth":request.form["birthmonth"][5:7],
        }
        bank = model.cohort(props)
        return render_template('results.html', props=props, bank=bank)
    else:
        return "error"
