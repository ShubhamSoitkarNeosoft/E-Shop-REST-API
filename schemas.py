import email
from unicodedata import name
from marshmallow import Schema,fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=False)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    brand = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str(required=True)
    rating = fields.Int(required=True)
    numReviews = fields.Int(required=False)
    price = fields.Int(required=True)
    countInStock = fields.Int(required=True)
    created_at = fields.Str(dump_only=True)

class PlainOrderSchema(Schema):
    id = fields.Int(dump_only=True)
    paymentMethod = fields.Str(required=True)
    taxPrice = fields.Float(required=True)
    shippingPrice = fields.Float(required=True)
    totalPrice = fields.Float(required=True)
    isPaid = fields.Bool(required=True)
    isDelivered = fields.Bool(required=True)
    created_at = fields.Str(dump_only=True)

class PlainOrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    qty = fields.Int(required=True)
    price = fields.Float(required=True)

# class PlainShippingAddressSchema(Schema):
#     id = fields.Int(dump_only=True)
#     address = fields.Str(required=True)
#     city = fields.Str(required=True)
#     postalCode = fields.Int(required=True)
#     country = fields.Str(required=True)
#     shippingPrice = fields.Float(required=True)


class ProductSchema(PlainProductSchema):
    user_id = fields.Int(required=True, load_only = True)
    # user = fields.Nested(UserSchema(),dump_only=True)

class OrderSchema(PlainOrderSchema):
    user_id = fields.Int(required=True, load_only = True)

class OrderItemSchema(PlainOrderItemSchema):
    order_id = fields.Int(required=True, load_only = True)
    product_id = fields.Int(required=True, load_only = True)

# class ShippingAddressSchema(PlainShippingAddressSchema):
#     # order_id = fields.Int(required=True, load_only = True)
#     pass





