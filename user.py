import os
import smtplib

from flask import Blueprint, Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from models.db import db
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from help_func import apology, login_required, isPhoneNumber, isHSPHemail

user = Blueprint('user', __name__)
db = SQL("sqlite:///webapp1.db")

@user.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Display complete transaction history
    #records = db.execute("SELECT * FROM submit_one WHERE user_id = :userID", userID=session["user_id"])

    #dict_hist = []
    #for record in records:

       # time = time["time"]
       # date = date["date"]
       # event_name = record["event_name"]
       # event_description = record["event_description"]
        #guest_count = guest_count["guest_count"]
       # contact_name = name["name"]
        #time = record["time"]
        #date = record["date"]
        #my_dict = {"time": time, "date": date, "event_name": event_name, "event_description" : event_description, "guest_count" : guest_count, "name": name}
        #dict_hist.append(my_dict)

    #return render_template("history.html", list=dict_hist)

    #return apology("Something is wrong.")

    #return redirect("/")


@user.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = :email",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@user.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@user.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE user_name = :username", username=request.form.get("username"))

        # Ensure username is unique
        if len(rows) >= 1:
            return apology("username already exists", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password and confirmation match
        if request.form.get("confirmation") != request.form.get("password"):
            return apology("must match password and confirm", 400)

        # TODO validate email
        raw_email = request.form.get("email")
        email = isHSPHemail(raw_email)


        #TODO validate phone
        raw_phone = request.form.get("phone")
        phone = isPhoneNumber(raw_phone)


        # Insert username into db
        db.execute("INSERT INTO users (user_name, hash, email, phone) VALUES (:username, :hashword, :email, :phone)",
                   username =request.form.get("username"), hashword = generate_password_hash(request.form.get("password")), email = request.form.get("email"), phone = request.form.get("phone"))


        '''confirmation_code = generate_password_hash(request.form.get("username"))
        confirm_code = confirmation_code[:7]

        #send email
        # have email include confirm_code
        # have email include link to http://ide50-vcoffee.cs50.io:8080/confirmregistration
        gmail_user = 'bi0staT.catering@gmail.com'
        gmail_password = 'biostats10'

        sent_from = gmail_user
        to = [email]
        subject = [confirm_code]
        body = 'Please enter the code in the subject lineinto the confirm registration page via the link below:  http://ide50-vcoffee.cs50.io:8080/confirmregistration\n\n'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()'''

    # Redirect user to home page
    return render_template("layout.html")




