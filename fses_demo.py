from datetime import timedelta
from flask import Flask, redirect, session, url_for

fsapp = Flask(__name__)

fsapp.config["SECRET_KEY"] = "sec"
fsapp.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=2)
fsapp.config["SESSION_REFRESH_EACH_REQUEST"] = False

"""
@fsapp.before_request
def before_request():
    session.permanent = True
    session.modified = True
"""

@fsapp.route("/")
def index():
    print(session.keys())
    return "Index"

@fsapp.route("/b")
def bindex():
    return "BIndex"

@fsapp.route("/login")
def login_usr():
    if not session.get("_user_name", None):
        # Check user_name & password from a form or something else 
        #   & the set a session cookie like below
        session["_user_name"] = "naz"
        session.permanent = True
    return redirect(url_for("index"))

@fsapp.route("/lg")
def lg():
    if session.get("_user_name", None):
        session.pop("_user_name")
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    fsapp.run(port=5006, debug=True)
