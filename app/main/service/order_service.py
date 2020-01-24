from app.main.model.order import get_all_buyer_orders, get_all_seller_orders, add_order, set_payment_flag, is_set_payment


def get_orders(args):
    """
    get all orders via user ID
    :param args: args contains the user type and user id
    :return: returns all the orders
    """
    user_id = args.get('id')
    if args.get('usrtype') == 'b':
        return get_all_buyer_orders(user_id)
    return get_all_seller_orders(user_id)


def place_order(data):
    """
    gets the order and adds order
    :param data: {"sellerId" : "13123qwer","cropId" : "12321adfads","quantity" : 10,"price" : 123.23,"buyerId": "asd1234asdf","paymentType": "paytm","deliveryType": "COD"}
    :return: {'status':success, 'orderId': 'asd214'} | {'status': 'fail', 'message': 'server problem'}
    """
    response = add_order(data)

    if response is None:
        response_object = {'status': 'fail', 'message': 'server problem'}
        return response_object, 409
    response_object = {'status':'success', 'orderId': response}
    return response_object, 201


def set_payment(data):
    """
    set the payment flag of the order
    :param data: contains the order Id
    :return: {'status': 'success'} | {"status" : "fail","message" : "Server Problem"}
    """
    order_id = data['orderId']
    if set_payment_flag(order_id):
        return {'status': 'success'}, 201
    return {"status": "fail", "message": "Server Problem"}, 409


def get_payment(args):
    """
    get the payment flag of the order
    :param args: contains the order Id of the order
    :return: {"status" : "success"} | {"status" : "fail","message" : "Server Problem"}
    """
    order_id = args.get('oId')

    return {'payment': is_set_payment(order_id)}, 201


def set_delivery(data):
    """
    set the deliver flag of the order
    :param data: contains the order Id
    :return: {'status': 'success'} | {"status" : "fail","message" : "Server Problem"}
    """
    order_id = data['orderId']
    if set_payment_flag(order_id):
        return {'status': 'success'}, 201
    return {"status": "fail", "message": "Server Problem"}, 409


def get_delivery(args):
    """
    get the payment flag of the order
    :param args: contains the order Id of the order
    :return: {"status" : "success"} | {"status" : "fail","message" : "Server Problem"}
    """
    order_id = args.get('oId')

    return {'delivery': is_set_payment(order_id)}, 201
