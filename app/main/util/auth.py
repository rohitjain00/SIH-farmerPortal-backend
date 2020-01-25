from .. import flask_bcrypt
import datetime
import jwt
from ..config import key


def password_hash(password):
    return flask_bcrypt.generate_password_hash(password).decode('utf-8')


def get_authentication_token(phone_number):
    """
    Creates a JWT token for users
    :param phone_number: phone numner to encode in
    :return: string
    """
    return encode_auth_token(phone_number)


def get_user_phone_number(token):
    """
    Returns the user from the token
    :param token: auth token of the user
    :return: phone number of the user
    """
    return decode_auth_token(token)


def encode_auth_token(phone_number):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': phone_number
        }
        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, key)
        is_blacklisted_token = get_authentication_token(auth_token)
        if is_blacklisted_token:
            return 'Token blacklisted. Please log in again.'
        else:
            return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def check_blacklist_token(token):
    """
    check and return if the user's token is in the blacklist collection
    :param token: auth token
    :return: boolean
    """
    pass
