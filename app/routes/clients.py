from flask import Blueprint, render_template, request, redirect, flash
from sqlalchemy.exc import IntegrityError
from ..models.contacts import Contacts
from ..database import db


client = Blueprint('client', __name__)


@client.route('/clients')
def clients_route():
    return render_template('clients/register_clients.html')


@client.route('/register/individual', methods=['POST',])
def register_client():

    try:
        first_name = request.form['name']
        last_name = request.form['surname']
        email = request.form['email']

        new_contact = Contacts(first_name=first_name, last_name=last_name, email=email)

        db.session.add(new_contact)
        db.session.commit()

        flash('Cliente cadastrado com sucesso!', 'success')

    except IntegrityError:
        flash("Endereço de email fornecido já está em uso no sistema.", 'danger')

    except Exception as e:
        flash("Erro ao cadastrar cliente no banco de dados: " + str(e), 'danger')

    finally:
        return redirect("/clients")
     