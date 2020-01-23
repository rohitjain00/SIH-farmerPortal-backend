import pymongo

from app.main import db

"""
To use database : 
    1. import the db variable from app.main
    2. check out the CRUD operation here : https://api.mongodb.com/python/current/tutorial.html
"""


def buyer_already_exist(phone_number):
    """
    Check if a buyer exists
    :param phone_number: phone Number of the user
    :return: boolean
    """
    if db.buyer.find({'phoneNumber': phone_number}).count() > 0:
        return True
    return False


def buyer_exist(phone_number, password):
    """
    Check if the buyer exist
    :param phone_number: Phone Number of the buyer
    :param password: Password of the user
    :return: boolean
    """
    if db.buyer.find({'phoneNumber': phone_number, 'password': password}).count() > 0:
        return True
    return False


def add_new_user(data):
    """
    Add new buyer to the database
    :param data: {'password' : 'asdf', 'phoneNumber': 90909090090, 'name': 'asdf', 'emailAddress': 'asddf@asdf.com'}
    :return: boolean
    """
    rec_id = db.buyer.insert_one(data)
    if db.buyer.find({"_id": rec_id.inserted_id}).count() > 0:
        return True
    return False


def get_authentication_token(phone_number):
    """
    Creates a token for the user with phone number
    :param phone_number: phone number to create authentication token of
    :return: string
    """
    return "temp_token"
