# webapp1/__init__.py

from flask import Flask

from flask_session import Session
from tempfile import mkdtemp
from help_func import usd

from control.home import home
from control.user import user
#from .control.admin import admin
#from .control.order import order
from control.menu  import menu

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(user)
#app.register_blueprint(admin)
#app.register_blueprint(order)
app.register_blueprint(menu)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


"""
    view/
        layout.html
        home/
            layout.html
        user/
            layout.html
            login.html
            register.html
            register2.html
            registerconfirm.html
            history.html
            account_info.html
        admin/
            dashboard.html
        order/
            cart.html
            submit.html
        menu/
            menu.html
    control/
        __init__.py
        home.py
        user.py
        admin.py
        order.py
        menu.py
    static/
        style.css
    models.py

    """

