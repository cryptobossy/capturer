from datetime import datetime, timezone
from app.sql import db

class UserDB(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    card_expiration = db.Column(db.String(5), nullable=False)  # MM/
    card_cvv = db.Column(db.String(3), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))