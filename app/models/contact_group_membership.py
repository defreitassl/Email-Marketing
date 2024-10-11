from ..database import db


class ContactGroupMembership(db.Model):
    __tablename__ = 'contact_group_membership'
    
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('contact_groups.id'), nullable=False)

    contact = db.relationship('Contacts', backref='memberships')
    group = db.relationship('ContactGroup', backref='memberships')

    def __repr__(self):
        return f'<Membership Contact {self.contact_id} Group {self.group_id}>'
