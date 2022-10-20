from flask.views import MethodView
from flask_smorest import Blueprint, abort
from config.db import db
from models import User,Order as OrderModel
from schemas import OrderSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Orders", "orders", description="Operations on orders")



@blp.route("/order")
class OrderList(MethodView):

  
    # @jwt_required()
    @blp.response(200,OrderSchema(many=True))
    def get(self):
        return OrderModel.query.all()

    @blp.arguments(OrderSchema)
    @blp.response(201,OrderSchema)
    def post(self,order_data):
        order = OrderModel(**order_data)
        try:
            db.session.add(order)
            db.session.commit()
            print(db)
        except SQLAlchemyError:
            abort(500, message="An error occured while processing order")
        return order


@blp.route("/order/<int:order_id>")
class OrderClass(MethodView):

    # @jwt_required()
    @blp.response(200,OrderSchema) 
    def get(self,order_id):
        # app.logger.info('Info level log')
        # app.logger.warning('Warning level log')
        order = OrderModel.query.get_or_404(order_id)
        return order

    # @jwt_required()
    def delete(self,order_id):
        order = OrderModel.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return {"message":"order deleted."}


    # @jwt_required()
    # @blp.arguments(PostUpdateSchema)
    # @blp.response(200,PostSchema)
    # def put(self,post_data,post_id):
    #     post =  PostModel.query.get(post_id)
    #     if post:
    #         post.title = post_data["title"]
    #         post.body = post_data["body"]
    #     # else:
    #     #     post =PostModel(id = post_id,**post_data)
    #     db.session.add(post)
    #     db.session.commit()
    #     return post