from app.main import db
from datetime import datetime 

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
    def add_order(data):
    """
    adds order to the database and creates a new order Id
    :param data: {"sellerId" : "13123qwer","cropId" : "12321adfads","quantity" : 10,"price" : 123.23,"buyerId": "asd1234asdf","paymentType": "paytm","deliveryType": "COD"}
    :return: None if unsuccessful insertion else return the unique Id of the order added
    """
    order = {}
    order['orderTo'] = data['buyerId']
    order['orderFrom'] = data['sellerId']
    order['crop'] = data['cropId']
    order['quantity'] = data['quantity']
    order['price'] = data['price']
    order['date'] = datetime.now()
    order['paymentDone'] = False    #default : False
    order['deliveryDone'] = False   #default : False
    order['paymentType'] = data['paymentType']
    order['deliveryType'] = data['deliveryType']
    #print(order)
    rec_id = db.order.insert_one(order)
    return rec_id.inserted_id
    return NULL


def set_payment_flag(order_id):
    """
    set the payment flag of the order to true
    :param order_id: order id of the order to set the flag of
    :return: return boolean
    """
    order_data = db.order.update_one({'_id' : order_id },{ '$set' : {'paymentDone' : True} } )
    order_data = db.order.find_one({"_id" : order_id})
    if(order_data['paymentDone']):
        return True
    return False


def is_set_payment(order_id):
    """
    check if the payment flag of the order is true
    :param order_id: order's id to check from
    :return: boolean
    """
    order = db.order.find_one({"_id" : order_id})
    if(order['paymentDone']):
        return True
    return False

def set_delivery_flag(order_id):
    """
    set the payment flag of the order to true
    :param order_id: order id of the order to set the flag of
    :return: return boolean
    """
    order_data = db.order.update_one({'_id' : order_id },{ '$set' : {'deliveryDone' : True} } )
    order_data = db.order.find_one({"_id" : order_id})
    if(order_data['deliveryDone']):
        return True
    return False


def is_set_delivery(order_id):
    """
    check if the payment flag of the order is true
    :param order_id: order's id to check from
    :return: boolean
    """
    order = db.order.find_one({"_id" : order_id})
    if(order['deliveryDone']):
        return True
    return False

