from flask import Blueprint, render_template, request

client = Blueprint('client', __name__)


@client.route('/clients')
def clients_route():
    return render_template('clients.html')


@client.route('/register', methods=['POST',])
def register_client():


    nome = request.form['name']
    email = request.form['email']

    return f"<p>Nome: {nome}</p><p>Email: {email}</p>"