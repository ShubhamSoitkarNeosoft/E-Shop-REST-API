from email.policy import default
from config.db import db



class OrderItem(db.Model):
    __tablename__ = "orderitem"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey("orders.id"),unique=False, nullable=False)
    product_id = db.Column(db.Integer,db.ForeignKey("products.id"),unique=False, nullable=False)
    name = db.Column(db.String(80),nullable=False)
    qty = db.Column(db.Integer,nullable=True,default=0)
    price = db.Column(db.Numeric(10,2), nullable=False)




