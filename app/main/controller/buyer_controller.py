from flask import request
from flask_restplus import Resource

from ..util.dto import BuyerDto
from ..service.buyer_service import register, login

api = BuyerDto.api
_buyer_login = BuyerDto.buyer_login
_buyer_register = BuyerDto.buyer_register


@api.route('/register')
class BuyerRegister(Resource):
    @api.response(201, "Buyer successfully created.")
    @api.doc("create a new buyer")
    @api.expect(_buyer_register, validate=True)
    def post(self):
        """Creates a new Buyer """
        print(request)
        data = request.json
        return register(data=data)


@api.route('/login')
class BuyerLogin(Resource):
    @api.doc("buyer login")
    @api.expect(_buyer_login, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return login(data=post_data)
