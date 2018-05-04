import os
import re

from flask import Blueprint, Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from models.db import db
from tempfile import mkdtemp

from help_func import usd

menu = Blueprint('menu', __name__)

db = SQL("sqlite:///webapp1.db")

def breakfast():

def lunch():

def pizza():

    pizza_dict = []
    copy_1 =
    pizzas =
        for pizza in pizzas:
            pizza_line = db.execute("SELECT * FROM menu_items WHERE subclass = PIZZA")
            append
            extras_dict =
            extras = db.execute("SELECT")
            append


def snacks():

def beverage():

    beverage_dict = []
    copy_1 = db.execute("SELECT * FROM")
    beverages =

def budget():

    budget_dict = []
    copy_1 = db.execute("SELECT * FROM menu_copy WHERE subclass = :budget", budget = budget)
    copy_hot_entrees = db.execute("SELECT * FROM ")
    hot_entrees = db.execute("SELECT * FROM")
    copy_salads =
    salads =
    copy_sides =
    extras =
    copy_snacks =
    snacks =
    beverage =
    # append to budget_dict

    ## hot_entrees, salads, extras, snacks, and beverage
    # hot entrees copy
    #salads, snacks, and sides
    budget_items = db.execute("SELECT * FROM menu_items WHERE class = :budget", budget = BUDGET)








@menu.route("/menu")
def index():

    # head_lines = db.execute("SELECT * FROM menu_items WHERE  text_form = :copy AND detailed_description = :header", copy = 2, header = header)
    rows = db.execute("SELECT * FROM menu_items WHERE text_form = :main_item", main_item = 0)
    # options = db.execute("SELECT * FROM meanu_items WHERE text_form = :options", options = 1)

    dict_menu = []
    for row in rows:
        description = row["description"]
        detailed_description = row["detailed_description"]
        price = row["price"] or 0
        my_dict = {"description" : description, "detailed_description" : detailed_description, "price" : price}
        dict_menu.append(my_dict)






    return render_template("menu.html", menu=dict_menu)

    #return apology("Something is wrong.")

    #return redirect("/")

   ## return render_template("menu.html")
          # event_name = record["event_name"]
       # event_description = record["event_description"]
        #guest_count = guest_count["guest_count"]
       # contact_name = name["name"]
        #time = record["time"]
        #date = record["date"]