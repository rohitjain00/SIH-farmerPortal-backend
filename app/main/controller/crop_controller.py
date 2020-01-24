from flask import request
from flask_restplus import Resource
from ..service.crop_service import get_crops, get_predicted_price, get_sellers, get_crop_rating, add_rating, \
    get_crop_availability, get_seller_inventory, add_to_seller_inventory, update_seller_inventory

from ..util.dto import CropDTO

api = CropDTO.api
_crop = CropDTO.crop
_crop_rating = CropDTO.crop_rating
_inventory_get = CropDTO.crop_inventory_get
_inventory_post = CropDTO.crop_inventory_post


@api.route("/")
class CropList(Resource):
    @api.doc("list_of_all_crops")
    @api.marshal_list_with(_crop, envelope="crops")
    def get(self):
        """List all crops"""
        return get_crops()


@api.route("/prediction")
class CropPrediction(Resource):
    @api.doc("predicted price of the crop")
    def get(self):
        """List all crops"""
        return get_predicted_price(request.args.get('cId'))


@api.route("/sellers")
class CropFarmers(Resource):
    @api.doc("farmers selling a particular crop")
    def get(self):
        """List of all farmers"""
        return get_sellers(request.args)


@api.route("/rating")
class CropRating(Resource):
    @api.doc("get rating of a particular crop")
    def get(self):
        """rating of a particular crop"""
        return get_crop_rating(request.args)

    @api.doc("add rating to the crop")
    @api.expect(_crop_rating, validate=True)
    def post(self):
        """add rating to the crop"""
        post_data = request.json
        return add_rating(data=post_data)


@api.route("/availability")
class CropAvailability(Resource):
    @api.doc("check availability of the product")
    def get(self):
        """check quantity of the crop"""
        return get_crop_availability(request.args)


@api.route("/inventory")
class CropInventory(Resource):
    @api.doc("get inventory of a seller")
    @api.marshal_list_with(_inventory_get, envelope='inventory')
    def get(self):
        """get inventory of the seller"""
        return get_seller_inventory(request.args)

    @api.doc("add new inventory to the seller")
    @api.expect(_inventory_post, validate=True)
    def post(self):
        """add new inventory to the seller"""
        post_data = request.json
        return add_to_seller_inventory(data=post_data)


@api.route("inventory/u")
class UpdateCropInventory(Resource):
    @api.doc("update inventory of the seller")
    @api.expect(_inventory_post, validate=True)
    def post(self):
        """add new inventory to the seller"""
        post_data = request.json
        return update_seller_inventory(data=post_data)
