from flask import Blueprint, render_template

client = Blueprint('client', __name__)


@client.route('/clients')
def clients_route():
    return render_template('clients.html')