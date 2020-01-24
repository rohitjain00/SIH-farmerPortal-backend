from app.main import db


def get_all_crops():
    """
    return all the crops from the database in form of [{'cropName': 'onion', 'cropId': '12312'}]
    :return: list of crops
    """
    pass


def get_price_prediction(cropId):
    """
    returns teh price prediction of the crop with crop Id
    :param cropId: crop ID of the crop
    :return: predicted price of the crop
    """
    pass


"""
all the get sellers method should return the data in this format
[
    {
        "sellerId" : "ad12asd21",
        "Name": "Asdf Asdf",
        "phoneNumber": "9079327009",
        "location" : [70.1313, 40.3443]
    }
]
"""


def get_all_sellers_by_distance(crop_id, min_qty, max_dis):
    """
    get sellers sorted by distance
    :param crop_id:
    :param min_qty:
    :param max_dis:
    :return:
    """
    pass


def get_all_sellers_by_rating(crop_id, min_qty, max_dis):
    """
    get sellers sorted by rating
    :param crop_id:
    :param min_qty:
    :param max_dis:
    :return:
    """
    pass


def get_all_sellers_by_delivery_time(crop_id, min_qty, max_dis):
    """
    get sellers sorted by delivery time
    :param crop_id:
    :param min_qty:
    :param max_dis:
    :return:
    """
    pass


def get_all_sellers(crop_id, min_qty, max_dis):
    """
    get all sellers without any sorting
    :param crop_id:
    :param min_qty:
    :param max_dis:
    :return:
    """
    pass


def get_rating(crop_id, seller_id):
    """
    get rating of the crop
    :param crop_id:
    :param seller_id:
    :return:
    """
    pass