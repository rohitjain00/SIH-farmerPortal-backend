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
    api = Namespace('crop', description='get crop methods')
    crop = api.model('crop', {
        'cropId': fields.String(required=True, description='unique ID of the crop'),
        'cropName': fields.String(required=True, description='cropName')
    })
    crop_rating = api.model('crop_rating', {
        'sellerId': fields.String(required=True, description='Seller Id of the product'),
        'cropId': fields.String(required=True, description='cropId of the crop'),
        'rating': fields.Integer(required=True, description='user provided rating to the product')
    })
    # crop_availability = api.model('crop_availability', {
    #     'sellerId': fields.String(required=True, description='Seller Id of the product'),
    #     'cropId': fields.String(required=True, description='cropId of the crop'),
    #     'quantity': fields.Float(required=True, description='quantity to check')
    # })
