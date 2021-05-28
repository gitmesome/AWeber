from datetime import datetime
from config import db


class Widget(db.Model):
    __tablename__ = "widget"
    widget_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    num_of_parts = db.Column(db.Iteger())
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
