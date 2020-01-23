from app.main import db

"""
To use database : 
    1. import the db variable from app.main
    2. check out the CRUD operation here : https://api.mongodb.com/python/current/tutorial.html
"""


def buyer_exist(phone_number):
    """
    Check if a buyer exists
    :param phone_number: phone Number of the user
    :return: boolean
    """
    return False


def buyer_exist(phone_number, password):
    """
    Check if the buyer exist
    :param phone_number: Phone Number of the buyer
    :param password: Password of the user
    :return: boolean
    """
    return True


def add_new_user(data):
    """
    Add new buyer to the database
    :param data: {'password' : 'asdf', 'phoneNumber': 90909090090, 'name': 'asdf', 'emailAddress': 'asddf@asdf.com'}
    :return: boolean
    """
    return True


def get_authentication_token(phone_number):
    """
    Creates a token for the user with phone number
    :param phone_number: phone number to create authentication token of
    :return: string
    """
    return "temp_token"
