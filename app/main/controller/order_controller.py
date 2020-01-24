from flask import request
from flask_restplus import Resource

from ..util.dto import OrderDTO
from ..service.order_service import get_orders, place_order, set_payment, get_payment, set_delivery, get_delivery

api = OrderDTO.api
_order = OrderDTO.order
_place_order = OrderDTO.place_order
_set_flag = OrderDTO.set_flag


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
    @api.doc("set the payment flag of the order")
    @api.expect(_set_flag, validate=True)
    def post(self):
        """payment flag set to true"""
        post_data = request.json
        return set_payment(data=post_data)

    @api.doc("get the payment flag of the order")
    def get(self):
        """get the payment flag of a particular order"""
        return get_payment(request.args)


@api.route('/delivery')
class OrderDeliver(Resource):
    @api.doc("set the delivery flag of the order")
    @api.expect(_set_flag, validate=True)
    def post(self):
        """delivery flag set to true"""
        post_data = request.json
        return set_delivery(data=post_data)

    @api.doc("get the delivery flag of the order")
    def get(self):
        """get the delivery flag of a particular order"""
        return get_delivery(request.args)
