from flask.views import MethodView
from flask_smorest import Blueprint, abort
from config.db import db
from models import User,Product
from schemas import ProductSchema
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify

blp = Blueprint("Products", "products", description="Operations on products")



@blp.route("/product")
class ProductList(MethodView):

  
    # @jwt_required()
    @blp.response(200,ProductSchema(many=True))
    def get(self):
        return Product.query.all()

    @blp.arguments(ProductSchema)
    @blp.response(201,ProductSchema)
    def post(self,product_data):
        product = Product(**product_data)
        # print("--------",product)
        try:
            db.session.add(product)
            db.session.commit()
            print(db)
        except SQLAlchemyError:
            abort(500, message="An error occured while adding the product")
        return product



@blp.route("/product/<int:product_id>")
class ProductClass(MethodView):
    
    @blp.response(200,ProductSchema)
    def get(self,product_id):
        product = Product.query.get_or_404(product_id)
        return product

    def delete(self,product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message":"product deleted."}


