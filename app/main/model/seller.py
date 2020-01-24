from app.main import db


def seller_already_exist(phoneNumber):
    """
    Check if the seller already exists
    :param phoneNumber: phone number of the seller
    :return: boolean
    """
    return True


def add_new_seller(data):
    """
    Add new seller to the database
    :param data: {"password": "asdfghjkl","phoneNumber": "9079327009","Name": "Asdf Asdf","location" : [70.1244, 40.1324],"deliveryUpto" : 15,"bankDetails" : {"upiID" : "asdf@okicici"}}
    :return: boolean
    """
    return True


def seller_exist(phoneNumber, password):
    """
    Check if the seller with same username and password exists in the database
    :param phoneNumber: phone number of the seller
    :param password: password of the seller
    :return: boolean
    """
    return True


def get_authentication_token(phoneNumber):
    return "temp_token"
