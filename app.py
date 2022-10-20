from flask import Flask
from config.db import db
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from resources.user import blp as UserBluePrint
from resources.product import blp as ProductBluePrint
from resources.order import blp as OrderBluePrint
from resources.orderItem import blp as OrderItemBluePrint
# from resources.shippingAddress import blp as ShippingAddressBluePrint
from flask_migrate import Migrate
import logging



app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"] = True



app.config["API_TITLE"] = "E-SHOP REST API"
app.config["API_VERSION"] = "v1"

    #openapi documentation version
app.config["OPENAPI_VERSION"] = "3.0.3"

    #Root url of openapi
app.config["OPENAPI_URL_PREFIX"] = "/"

    #Below code tells flask smorest to use swagger for api documentation
app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopdata.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.config["JWT_SECRET_KEY"] = "shubham"
jwt = JWTManager(app)



@app.before_first_request
def create_tables():
    db.create_all()

  
api = Api(app)

api.register_blueprint(UserBluePrint)
api.register_blueprint(ProductBluePrint)
api.register_blueprint(OrderBluePrint)
api.register_blueprint(OrderItemBluePrint)
# api.register_blueprint(ShippingAddressBluePrint)


logging.basicConfig(level=logging.DEBUG, 
format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

