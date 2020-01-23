from app.main.model.buyer import buyer_exist, add_new_user, get_authentication_token


def register(data):
    """
    check if the user exists in the database and if not registers the user to the database
    :param data: {'password' : 'asdf', 'phoneNumber': 90909090090, 'name': 'asdf', 'emailAddress': 'asddf@asdf.com'}
    :return: {'status' : 'success' | 'failure', "authenticationToken" : "asdfasdkjfhaljhfalskdjfghoq782364ro8qwyhraiwy37842qy"}
    """
    if buyer_exist(data.phoneNumber):
        return get_fail_message('phone number already exists'), 409
    has_added = add_new_user(data)
    if has_added:
        response_object = {
            'status': 'success',
            'authenticationToken': get_authentication_token(data.phoneNumber)
        }
        return response_object, 201


def login(data):
    """
    checks the login information and return authentication token on success
    :param data: {'phoneNumber': 'asdf', 'password': '12313'}
    :return: {'status' : 'success' | 'failure', "authenticationToken" : "asdfasdkjfhaljhfalskdjfghoq782364ro8qwyhraiwy37842qy"}
    """
    if buyer_exist(data.phoneNumber, data.password):
        response_object = {
            'status': 'success',
            'authenticationToken': get_authentication_token(data.phoneNumber)
        }
        return response_object, 201
    return get_fail_message("user not present")


def get_fail_message(error_message):
    return {"status": "fail", "message": error_message}
