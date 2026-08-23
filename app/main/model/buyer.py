from app.main import get_db
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
    if get_db().buyer.find({'phoneNumber': phone_number}).count() > 0:
        return True
    return False


def buyer_exist(phone_number, password):
    """
    Check if the buyer exist
    :param phone_number: Phone Number of the buyer
    :param password: Password of the user
    :return: boolean
    """
    if get_db().buyer.find({'phoneNumber': phone_number, 'password': password}).count() > 0:
        return True
    return False


def add_new_buyer(data):
    """
    Add new buyer to the database
    :param data: {'password' : 'asdf', 'phoneNumber': 90909090090, 'name': 'asdf', 'emailAddress': 'asddf@asdf.com'}
    :return: boolean
    """
         
    # Adding extra field for storing date/Time in the record
    today = datetime.now()
    data['registeredDateTime'] = today
    rec_id = get_db().buyer.insert_one(data)
    if get_db().buyer.find({ "_id" : rec_id.inserted_id}).count() > 0: 
        return True
    return False


def get_registered_date_time(buyer_id):
    """
    Get the Registered date of the buyer
    :param buyer_id:
    :return: boolean -- if buyer doesn't exist
             string -- containing date/Time
    """
    if get_db().buyer.find({'_id': buyer_id }).count() > 0:
        data = get_db().buyer.find_one({'_id': buyer_id })
        date = data['registeredDateTime']
        date = date.strftime("%d/%m/%Y %H:%M:%S")
        return date
    return False
