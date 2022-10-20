from flask.views import MethodView
from flask_smorest import Blueprint, abort
from config.db import db
from models import User,OrderItem as OrderItemModel
from schemas import OrderItemSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("OrderItems", "orderitems", description="Operations on order items")




@blp.route("/order-item")
class OrderItemList(MethodView):

  
    # @jwt_required()
    @blp.response(200,OrderItemSchema(many=True))
    def get(self):
        return OrderItemModel.query.all()

    @blp.arguments(OrderItemSchema)
    @blp.response(201,OrderItemSchema)
    def post(self,order_data):
        order = OrderItemModel(**order_data)
        try:
            db.session.add(order)
            db.session.commit()
            print(db)
        except SQLAlchemyError:
            abort(500, message="An error occured while processing order")
        return order



@blp.route("/order-item/<int:orderitem_id>")
class OrderItemClass(MethodView):

    # @jwt_required()
    @blp.response(200,OrderItemSchema) 
    def get(self,orderitem_id):
        # app.logger.info('Info level log')
        # app.logger.warning('Warning level log')
        order = OrderItemModel.query.get_or_404(orderitem_id)
        return order

    # @jwt_required()
    def delete(self,orderitem_id):
        order = OrderItemModel.query.get_or_404(orderitem_id)
        db.session.delete(order)
        db.session.commit()
        return {"message":"item deleted."}