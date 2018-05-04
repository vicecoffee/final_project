import csv
import os
import urllib.request
import re

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def isPhoneNumber(raw_phone):
    raw_phone_list = []
    for i in raw_phone:
        if i.isnumeric():
            raw_phone_list.append(i)
    if raw_phone_list[0:5] is not [6,1,7,4,3,2]:
        return apology("must be a HSPH phone number", 400)
    phone = join(raw_phone_list)
    return(phone)

def isHSPHemail(raw_email):
    test_domain = raw_email.split("@")
    if test_domain[1] is not ["hsph.harvard.edu"]:
        return apology("must have hsph email account", 400)
    email = join(test_domain)
    return true



