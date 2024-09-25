from ..database import db


class EmailCampaign(db.Model):
    __tablename__ = 'email_campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(100), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey('email_templates.id'), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('scheduled', 'sent', 'failed'), default='scheduled')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    template = db.relationship('EmailTemplate', backref='campaigns')

    def __repr__(self):
        return f'<EmailCampaign {self.campaign_name}>'
