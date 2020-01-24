from app.main import db


def get_all_buyer_orders(buyer_id):
    """
    get all order of buyer sorted by date in descending order
    :param buyer_id: id of the buyer
    :return: List of {"orderId" : "adfasd102938","sellerName" : "Asdf Asdf","sellerPhoneNumber" : 90909439033"cropName" : "onion","quantity" : 10,"date" : 2012-04-23T18:25:43.511Z,"paymentStatus" : True,"deliver" : True}
    """
    pass


def get_all_seller_orders(seller_id):
    """
    get all order of seller sorted by date in descending order
    :param seller_id: id of the buyer
    :return: List of {"orderId" : "adfasd102938","sellerName" : "Asdf Asdf","sellerPhoneNumber" : 90909439033"cropName" : "onion","quantity" : 10,"date" : 2012-04-23T18:25:43.511Z,"paymentStatus" : True,"deliver" : True}
    """
    pass


def add_order(data):
    """
    adds order to the database and creates a new order Id
    :param data: {"sellerId" : "13123qwer","cropId" : "12321adfads","quantity" : 10,"price" : 123.23,"buyerId": "asd1234asdf","paymentType": "paytm","deliveryType": "COD"}
    :return: None if unsuccessful insertion else return the unique Id of the order added
    """
    pass


def set_payment_flag(order_id):
    """
    set the payment flag of the order to true
    :param order_id: order id of the order to set the flag of
    :return: return boolean
    """
    pass


def is_set_payment(order_id):
    """
    check if the payment flag of the order is true
    :param order_id: order's id to check from
    :return: boolean
    """
    pass

def set_delivery_flag(order_id):
    """
    set the payment flag of the order to true
    :param order_id: order id of the order to set the flag of
    :return: return boolean
    """
    pass


def is_set_delivery(order_id):
    """
    check if the payment flag of the order is true
    :param order_id: order's id to check from
    :return: boolean
    """
    pass

