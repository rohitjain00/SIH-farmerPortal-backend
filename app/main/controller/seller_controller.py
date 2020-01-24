from flask import request
from flask_restplus import Resource

from ..util.dto import SellerDTO
from ..service.seller_service import register, login

api = SellerDTO.api
_seller_login = SellerDTO.seller_login
_seller_registration = SellerDTO.seller_registration


@api.route('/register')
class SellerRegister(Resource):
    @api.response(201, "Seller successfully created.")
    @api.doc("create a new seller")
    @api.expect(_seller_registration, validate=True)
    def post(self):
        """Creates a new Seller """
        print(request)
        data = request.json
        return register(data=data)


@api.route('/login')
class SellerLogin(Resource):
    @api.doc("buyer login")
    @api.expect(_seller_login, validate=True)
    def post(self):
        """Login to seller"""
        post_data = request.json
        return login(data=post_data)
