from ..database import db


class CampaignRecipient(db.Model):
    __tablename__ = 'campaign_recipients'
    
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('email_campaigns.id'), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    opened = db.Column(db.Boolean, default=False)
    clicked = db.Column(db.Boolean, default=False)

    campaign = db.relationship('EmailCampaign', backref='recipients')
    contact = db.relationship('Contact', backref='received_campaigns')

    def __repr__(self):
        return f'<CampaignRecipient Campaign {self.campaign_id} Contact {self.contact_id}>'
