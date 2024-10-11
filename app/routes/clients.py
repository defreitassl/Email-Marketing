from flask import Blueprint, render_template, request, redirect, flash
from sqlalchemy.exc import IntegrityError
from ..models.contacts import Contacts
from ..models.contact_groups import ContactGroup
from ..models.contact_group_membership import ContactGroupMembership
from ..database import db


def associate_contact_and_group(contact: Contacts, group: ContactGroup) -> ContactGroupMembership:

    contact_id = contact.id
    group_id = group.id

    association = ContactGroupMembership(contact_id=contact_id, group_id=group_id)

    return association


client = Blueprint('client', __name__)


@client.route('/register/client')
def clients_route():

    groups = db.session.query(ContactGroup).all()
    return render_template('clients/register_clients.html', groups=groups)


@client.route('/register/client/individual', methods=['POST',])
def register_client():

    try:
        first_name = request.form['name']
        last_name = request.form['surname']
        email = request.form['email']
        group_name = request.form['categoryInput']

        if all([first_name, last_name, email]):

            new_contact = Contacts(first_name=first_name, last_name=last_name, email=email)
            db.session.add(new_contact)

            if group_name:
                group = ContactGroup(group_name=group_name)
                db.session.add(group)
            else:
                group_name = request.form['categorySelect']
                group = db.session.query(ContactGroup).filter_by(group_name=group_name).first()

            db.session.flush()
            group_association = associate_contact_and_group(contact=new_contact, group=group)

            if group_association:
                db.session.add(group_association)

            db.session.commit()
            flash('Cliente cadastrado com sucesso!', 'success')
        
        else:
            flash('Preencha todos os campos antes de continuar.', 'danger')

    except IntegrityError as e:
        db.session.rollback()
        flash("Endereço de email fornecido já está em uso no sistema.", 'danger')

    except Exception as e:
        db.session.rollback()
        flash("Erro ao cadastrar cliente no banco de dados: " + str(e), 'danger')

    finally:
        return redirect("/register/client")
     