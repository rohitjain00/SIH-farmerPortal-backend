from flask import Flask
from flask_bcrypt import Bcrypt
from pymongo import MongoClient


from .config import config_by_name

db = None
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    global db
    db = MongoClient(config_by_name[config_name].MONGODB_URL)
    flask_bcrypt.init_app(app)

    return app
