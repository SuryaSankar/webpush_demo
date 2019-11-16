from .core import db


class PushSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subscription_json = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
