from ..model.crop import get_all_crops, get_price_prediction, get_all_sellers_by_distance, get_all_sellers_by_rating, \
    get_all_sellers_by_delivery_time, get_all_sellers, get_rating, add_rating_crop, is_crop_available

from .seller_service import get_fail_message


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


def get_sellers(args):
    """
    get sellers of a particular crop
    :param args: args in the request
    :return: return a list of sellers
    """
    crop_id = args.get('cId')
    min_qty = args.get('mqty')
    sort_by = args.get('s')
    max_dis = args.get('md')

    if sort_by == 'dis':
        return get_all_sellers_by_distance(crop_id, min_qty, max_dis)
    elif sort_by == 'r':
        return get_all_sellers_by_rating(crop_id, min_qty, max_dis)
    elif sort_by == 'del':
        return get_all_sellers_by_delivery_time(crop_id, min_qty, max_dis)
    return get_all_sellers(crop_id, min_qty, max_dis)


def get_crop_rating(args):
    """
    get crop rating
    :param args: args with the get request
    :return: return the rating of the crops
    """
    crop_id = args.get('cId')
    seller_id = args.get('sId')
    return get_rating(crop_id, seller_id)


def add_rating(data):
    """
    add rating to the product
    :param data: data contains the sellerId, cropId, rating of the product
    :return: return success | failure
    """
    seller_id = data['sellerId']
    crop_id = data['cropId']
    rating = data['rating']

    if add_rating_crop(seller_id, crop_id, rating):
        response_object = {
            'status': 'success'
        }
        return response_object, 201
    return get_fail_message("Unable to add rating"), 409

def get_crop_availability(args):
    """
    check and return crop availability
    :param args: args contains seller id, crop id, quantity
    :return: {"status": "avaialble" | "unavailable"}
    """
    seller_id = args.get('sId')
    crop_id = args.get('cId')
    quantity = args.get('qty')
    if is_crop_available(seller_id, crop_id, quantity):
        response_object = {
            "status": "available"
        }
        return response_object, 200
    response_object = {
        "status" : "unavailable"
    }
    return response_object, 200
