from flask import Blueprint, render_template


presentation = Blueprint('presentation', __name__)


@presentation.route('/')
def presentation_page():
    return render_template('presentation_page.html')