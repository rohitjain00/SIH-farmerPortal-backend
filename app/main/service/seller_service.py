from app.main.model.seller import seller_already_exist, add_new_seller, seller_exist
from app.main.util.auth import password_hash, get_authentication_token


def register(data):
    """
    check if the seller exists in the database and if not registers the seller to the database
    :param data: {"password": "asdfghjkl","phoneNumber": "9079327009","Name": "Asdf Asdf","location" : [70.1244, 40.1324],"deliveryUpto" : 15,"bankDetails" : {"upiID" : "asdf@okicici"}}
    :return: {'status' : 'success' | 'failure', "authenticationToken" : "asdfasdkjfhaljhfalskdjfghoq782364ro8qwyhraiwy37842qy"}
    """
    if seller_already_exist(data['phoneNumber']):
        return get_fail_message('phone number already exists'), 409
    data['password'] = password_hash(data['password'])
    has_added = add_new_seller(data)
    if has_added:
        response_object = {
            'status': 'success',
            'authenticationToken': get_authentication_token(data['phoneNumber'])
        }
        return response_object, 201


def login(data):
    """
    checks the login information and return authentication token on success
    :param data: {'phoneNumber': 'asdf', 'password': '12313'}
    :return: {'status' : 'success' | 'failure', "authenticationToken" : "asdfasdkjfhaljhfalskdjfghoq782364ro8qwyhraiwy37842qy"}
    """
    data['password'] = password_hash(data['password'])
    if seller_exist(data['phoneNumber'], data['password']):
        response_object = {
            'status': 'success',
            'authenticationToken': get_authentication_token(data['phoneNumber'])
        }
        return response_object, 201
    return get_fail_message("user not present")


def get_fail_message(error_message):
    return {"status": "fail", "message": error_message}
