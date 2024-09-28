from flask import render_template, Blueprint


learn_more = Blueprint("learn_more", __name__)

@learn_more.route('/learn-more')
def lear_more_page():
    return render_template('learn_more.html')