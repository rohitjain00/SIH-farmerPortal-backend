# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.buyer_controller import api as buyer_ns
from .main.controller.seller_controller import api as seller_ns
from .main.controller.crop_controller import api as crop_ns
from .main.controller.order_controller import api as order_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SIH-farmer-portal-api',
          version='1.0',
          description='backend for SIH-farmer-portal'
          )

api.add_namespace(buyer_ns, path='/buyer')
api.add_namespace(seller_ns, path='/seller')
api.add_namespace(crop_ns, path='/crop')
api.add_namespace(order_ns, path='/order')
