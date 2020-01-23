# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.buyer_controller import api as buyer_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SIH-farmer-portal-api',
          version='1.0',
          description='backend for flask'
          )

api.add_namespace(buyer_ns, path='/buyer')
