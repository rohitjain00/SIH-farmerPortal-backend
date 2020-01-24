from flask import request
from flask_restplus import Resource

from ..util.dto import OrderDTO
from ..service.order_service import get_orders, place_order

api = OrderDTO.api
_order = OrderDTO.order
_place_order = OrderDTO.place_order


@api.route('/')
class OrderList(Resource):
    @api.doc("list_of_all_orders")
    @api.marshal_list_with(_order, envelope="orders")
    def get(self):
        """List all crops"""
        return get_orders(request.args)

    @api.doc("place a new order")
    @api.expect(_place_order, validate=True)
    def post(self):
        post_data = request.json
        return place_order(post_data)


@api.route('/payment')
class OrderPayment(Resource):
    @api.doc("buyer login")
    @api.expect(_place_order, validate=True)
    def post(self):
        """"""""
        post_data = request.json
        return login(data=post_data)
