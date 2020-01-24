from flask_restplus import Namespace, fields


class BuyerDto:
    api = Namespace('buyer', description='Buyer login register related operations')
    buyer_register = api.model('buyer_register', {
        'phoneNumber': fields.Integer(required=True, description='buyer\'s phone number'),
        'password': fields.String(required=True, description='buyer\'s password'),
        'name': fields.String(required=True, description='buyer\'s name'),
        'emailAddress': fields.String(required=True, description='buyer\'s email')
    })
    buyer_login = api.model('buyer_login', {
        'phoneNumber': fields.Integer(required=True, description='buyer\'s phone number'),
        'password': fields.String(required=True, description='buyer\'s password')
    })


class SellerDTO:
    api = Namespace('seller', description='Seller login register related operations')
    bank_details = api.model('bank', {
        'upiID': fields.String(required=True, description='UPI id of the seller')
    })
    seller_registration = api.model('seller_registration', {
        'phoneNumber': fields.Integer(required=True, description='seller\'s phone number'),
        'password': fields.String(required=True, description='seller\'s password'),
        'name': fields.String(required=True, description='seller\'s name'),
        'location': fields.List(fields.Float, required=True, description='co-ordinates of the Seller, list the longitude first and then latitude'),
        'deliveryUpto': fields.Float(required=True, description='delivery upto in KMs'),
        'bankDetails': fields.Nested(bank_details)
    })
    seller_login = api.model('seller_login', {
        'phoneNumber': fields.Integer(required=True, description='seller\'s phone number'),
        'password': fields.String(required=True, description='seller\'s password')
    })


class CropDTO:
    api = Namespace('crop', description='crop related operations')
    crop = api.model('crop', {
        'cropId': fields.String(required=True, description='unique ID of the crop'),
        'cropName': fields.String(required=True, description='cropName')
    })
    crop_rating = api.model('crop_rating', {
        'sellerId': fields.String(required=True, description='Seller Id of the product'),
        'cropId': fields.String(required=True, description='cropId of the crop'),
        'rating': fields.Integer(required=True, description='user provided rating to the product')
    })


class OrderDTO:
    api = Namespace('order', description='order related operations')
    order = api.model('order', {
        "orderId": fields.String(required=True, description="order Id of the order"),
        "sellerName": fields.String(required=True, description="seller's name"),
        "sellerPhoneNumber": fields.Integer(required=True, description="seller's phone number"),
        "cropName": fields.String(required=True, description="crop name that was sold"),
        "quantity": fields.Float(required=True, description="quantity purchased"),
        "date": fields.DateTime(required=True, description="date time of the order placed"),
        "paymentStatus": fields.Boolean(required=True, description="payment flag"),
        "deliver": fields.Boolean(required=True, description="delivery flag")
    })
    place_order = api.model('place_order', {
        'sellerId': fields.String(required=True, description='Id of the seller selling the crop'),
        'cropId': fields.String(required=True, description='Id of the crop that is sold'),
        'quantity': fields.Float(required=True, description='quantity sold in Kgs'),
        'price': fields.Float(required=True, description='price at selling time'),
        'buyerId': fields.Float(required=True, description='Id of the buyer buying the crop'),
        'paymentType': fields.String(required=True, description='payment mode of the order'),
        'deliveryType': fields.String(required=True, description='delivery type of the order')
    })
    set_flag = api.model('set_flag', {
        'orderId': fields.String(required=True, description='order id of the order to change flags of')
    })
