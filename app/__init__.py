# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.buyer_controller import api as buyer_ns
from .main.controller.seller_controller import api as seller_ns
from .main.controller.crop_controller import api as crop_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SIH-farmer-portal-api',
          version='1.0',
          description='backend for flask'
          )

api.add_namespace(buyer_ns, path='/buyer')
api.add_namespace(seller_ns, path='/seller')
api.add_namespace(crop_ns, path='/crop')
