from cs50 import SQL
import os.path as path
import sys

one_up =  path.join(__file__ ,"../..")
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///webapp1.db")