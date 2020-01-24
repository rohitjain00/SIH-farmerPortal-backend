from ..model.crop import get_all_crops, get_price_prediction, get_all_sellers_by_distance, get_all_sellers_by_rating, \
    get_all_sellers_by_delivery_time, get_all_sellers, get_rating


def get_crops():
    """
    return all the crops from the database in form of [{'cropName': 'onion', 'cropId': '12312'}]
    :return: list of crops
    """
    return get_all_crops()


def get_predicted_price(crop_id):
    """
    Get the predicted price of the crop
    :param: cropId of the crop
    :return: predicted value of the crop
    """
    request_object = {
        'predictedPrice': get_price_prediction(crop_id)
    }
    return request_object


def get_sellers(crop_id, min_qty, sort_by, max_dis):
    """
    get sellers of a particular crop
    :param crop_id: crop Id to fetch sellers of
    :param min_qty: min qty required by the user
    :param sort_by: type of sorting ('dis' : distance, 'r': rating, 'del': 'delivery Time')
    :param max_dis: max Distance from the user
    :return: return a list of sellers
    """
    if sort_by == 'dis':
        return get_all_sellers_by_distance(crop_id, min_qty, max_dis)
    elif sort_by == 'r':
        return get_all_sellers_by_rating(crop_id, min_qty, max_dis)
    elif sort_by == 'del':
        return get_all_sellers_by_delivery_time(crop_id, min_qty, max_dis)
    return get_all_sellers(crop_id, min_qty, max_dis)


def get_crop_rating(crop_id, seller_id):
    """
    get the rating of the crop of a seller
    :param crop_id: crop id of the crop
    :param seller_id: seller id of the crop's owner
    :return: {"rating" : 4,"count" : 34}
    """
    return get_rating(crop_id, seller_id)
