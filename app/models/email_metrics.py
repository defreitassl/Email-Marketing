from ..database import db


class EmailMetrics(db.Model):
    __tablename__ = 'email_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('email_campaigns.id'), nullable=False)
    total_sent = db.Column(db.Integer, default=0)
    total_opened = db.Column(db.Integer, default=0)
    total_clicked = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    campaign = db.relationship('EmailCampaign', backref='metrics')

    def __repr__(self):
        return f'<EmailMetrics Campaign {self.campaign_id}>'
