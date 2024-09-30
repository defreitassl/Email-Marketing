from flask import render_template, Blueprint

home = Blueprint("home", __name__)


@home.route('/home')
def home_page():
    return render_template('home_page.html')