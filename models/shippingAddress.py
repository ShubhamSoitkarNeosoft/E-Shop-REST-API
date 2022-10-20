# from config.db import db
# from datetime import datetime


# class ShippingAddress(db.Model):
#     __tablename__ = "shipping-address"

#     id = db.Column(db.Integer, primary_key=True)
#     # order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
#     address = db.Column(db.String(80),nullable=True)
#     city = db.Column(db.String(80),nullable=True)
#     postalCode = db.Column(db.Integer,nullable=False)
#     country = db.Column(db.String(80),nullable=False)
#     shippingPrice = db.Column(db.Numeric(10,2), nullable=True)
