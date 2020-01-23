from flask_restplus import Namespace, fields


class buyerDto:
    api = Namespace('buyer', description='user related operations')
    buyer_register = api.model('buyer_register', {
        'phoneNumber': fields.Integer(required=True, description='user\'s phone number'),
        'password': fields.String(required=True, description='user\'s password'),
        'name': fields.String(required=True, description='user\'s name'),
        'emailAddress': fields.String(required=True, description='user\'s email')
    })
    buyer_login = api.model('buyer_login', {
        'phoneNumber': fields.Integer(required=True, description='user\'s phone number'),
        'password': fields.String(required=True, description='user\'s password')
    })

