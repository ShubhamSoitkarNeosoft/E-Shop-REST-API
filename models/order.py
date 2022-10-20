from config.db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),unique=False, nullable=False)
    paymentMethod = db.Column(db.String(80),nullable=False)
    taxPrice = db.Column(db.Numeric(10,2), nullable=True)
    shippingPrice = db.Column(db.Numeric(10,2), nullable=True)
    totalPrice = db.Column(db.Numeric(10,2), nullable=True)
    isPaid = db.Column(db.Boolean, nullable=True)
    isDelivered = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # shipping_address= db.relationship("shipping-address", uselist=False, backref="image")