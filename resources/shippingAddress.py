# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from config.db import db
# from models import shippingAddress as ShippingAddressModel
# from schemas import ShippingAddressSchema
# from sqlalchemy.exc import SQLAlchemyError
# from flask import jsonify

# blp = Blueprint("ShippingAddress", "shipping-address", description="Operations on shipping address")



# @blp.route("/address")
# class ProductList(MethodView):

  
#     # @jwt_required()
#     @blp.response(200,ShippingAddressSchema(many=True))
#     def get(self):
#         return ShippingAddressModel.query.all()

#     @blp.arguments(ShippingAddressSchema)
#     @blp.response(201,ShippingAddressSchema)
#     def post(self,address_data):
#         address = ShippingAddressModel(**address_data)
#         # print("--------",address)
#         try:
#             db.session.add(address)
#             db.session.commit()
#             print(db)
#         except SQLAlchemyError:
#             abort(500, message="An error occured while adding the address")
#         return address