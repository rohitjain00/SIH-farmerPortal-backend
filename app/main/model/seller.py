from app.main import db


def seller_already_exist(phone_number):
    """
    Check if the seller already exists
    :param phoneNumber: phone number of the seller
    :return: boolean
    """
    if db.seller.find({'phoneNumber': phone_number}).count() > 0:
        return True
    return False


def add_new_seller(data):
    """
    Add new seller to the database
    :param data: {"password": "asdfghjkl","phoneNumber": "9079327009","Name": "Asdf Asdf","location" : [70.1244, 40.1324],"deliveryUpto" : 15,"bankDetails" : {"upiID" : "asdf@okicici"}}
    :return: boolean
    """
    rec_id = db.seller.insert_one(data)
    if db.seller.find({ "_id" : rec_id.inserted_id}).count() > 0: 
        return True
    return False
    

def seller_exist(phone_number, password):
    """
    Check if the seller with same username and password exists in the database
    :param phone_number: phone number of the seller
    :param password: password of the seller
    :return: boolean
    """
    if db.seller.find({'phoneNumber': phone_number, 'password': password}).count() > 0:
        return True
    return False
