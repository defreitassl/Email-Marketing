from ..database import db


class ContactGroup(db.Model):
    __tablename__ = 'contact_groups'
    
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<ContactGroup {self.group_name}>'