import os
from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
# if os.path.exists("env.py"):
# import env

# it should work using env.py
# app.secret_key = os.environ.get("SECRET_KEY")    instead of "runko"
app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.secret_key = "runko"


mongo = PyMongo(app)


@app.route('/')
@app.route('/index_recipe')
def index_recipe():

    """
    On page load, index page is displayed.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
