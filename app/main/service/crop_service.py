from ..model.crop import get_all_crops, get_price_prediction, get_all_sellers_by_distance, get_all_sellers_by_rating, \
    get_all_sellers_by_delivery_time, get_all_sellers, get_rating, add_rating_crop, is_crop_available, get_inventory, add_inventory, update_inventory

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
    longitude = args.get('lon')
    latitude = args.get('lat')
    if sort_by == 'dis':
        return get_all_sellers_by_distance(crop_id, min_qty, max_dis, longitude, latitude)
    elif sort_by == 'r':
        return get_all_sellers_by_rating(crop_id, min_qty, max_dis, longitude, latitude)
    elif sort_by == 'del':
        return get_all_sellers_by_delivery_time(crop_id, min_qty, max_dis, longitude, latitude)
    return get_all_sellers(crop_id, min_qty, max_dis, longitude, latitude)


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


def get_seller_inventory(args):
    """
    returns the inventory of the seller
    :param args: contains the seller's id
    :return: return a list of the crops and quantity
    """
    seller_id = args.get('sId')
    return get_inventory(seller_id)


def add_to_seller_inventory(data):
    """
    adds to the inventory of the seller
    :param data: {"cropId" : "123asdf","sellerId": "2134@324""quantity" : 1000.132,"price" : 123.123}
    :return: {"status" : "success"} | {"status": "fail","message": "Server Problem"}
    """
    crop_id = data['cropId']
    seller_id = data['sellerId']
    quantity = data['quantity ']
    price = data['price']
    if add_inventory(crop_id, seller_id, quantity, price):
        return {"status" : "success"}, 201
    return {"status": "fail", "message": "Server Problem"}, 409


def update_seller_inventory(data):
    """
    adds to the inventory of the seller
    :param data: {"cropId" : "123asdf","sellerId": "2134@324""quantity" : 1000.132,"price" : 123.123}
    :return: {"status" : "success"} | {"status": "fail","message": "Server Problem"}
    """
    crop_id = data['cropId']
    seller_id = data['sellerId']
    quantity = data['quantity ']
    price = data['price']
    if update_inventory(crop_id, seller_id, quantity, price):
        return {"status" : "success"}, 201
    return {"status": "fail", "message": "Server Problem"}, 409
