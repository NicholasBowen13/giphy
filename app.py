# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods = ["GET", "POST"])
def yourgif():
    user_response = request.form["gifchoice"]
    message =getImageUrlFrom(user_response)
    return render_template("yourgif.html", time=datetime.now(), message = message)
    #add datetime.now() browser to trick our browser into updating the css if we make any changes

    