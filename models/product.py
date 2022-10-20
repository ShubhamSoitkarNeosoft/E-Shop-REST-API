
from config.db import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    brand = db.Column(db.String(80),nullable=False)
    category = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(120),nullable=False)
    rating = db.Column(db.Numeric(10,2), nullable=True)
    numReviews = db.Column(db.Integer,nullable=True)
    price = db.Column(db.Integer,nullable=True)
    countInStock = db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),unique=False, nullable=False)
    user = db.relationship("User",back_populates="products")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)