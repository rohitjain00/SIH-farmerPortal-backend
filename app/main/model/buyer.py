from app.main import db
from datetime import date , datetime

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


def add_new_buyer(data):
    """
    Add new buyer to the database
    :param data: {'password' : 'asdf', 'phoneNumber': 90909090090, 'name': 'asdf', 'emailAddress': 'asddf@asdf.com'}
    :return: boolean
    """
    
    """
    For Adding Date and Time Both  
    today = datetime.now()
    d1 = today.strftime("%d/%m/%Y %H:%M:%S")
    data['registeredDateTime'] = d1
    """
    
    #Adding extra field for storing date in the record 
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    data['registeredDate'] = d1
    
    rec_id = db.buyer.insert_one(data)
    if db.buyer.find({ "_id" : rec_id.inserted_id}).count() > 0: 
        return True
    return False

def getRegisteredDate(phoneNumber):
    """
    Get the Registered date of the buyer 
        -param : phoneNumber (as it is the unique-id used in database)
        -return: boolean -- if buyer doesn't exist
                 date -- if user exist
    """
    if db.buyer.find({'phoneNumber': phoneNumber}).count() > 0:
        data = db.buyer.find_one({'phoneNumber': phoneNumber})
        return data['registeredDate'];
    return False


def get_authentication_token(phone_number):
    """
    Creates a token for the user with phone number
    :param phone_number: phone number to create authentication token of
    :return: string
    """
    return "temp_token"
