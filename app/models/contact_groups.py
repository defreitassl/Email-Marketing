from ..database import db


class ContactGroup(db.Model):
    __tablename__ = 'contact_groups'
    
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<ContactGroup {self.group_name}>'