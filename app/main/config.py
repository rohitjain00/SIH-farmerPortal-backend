import os


basedir = os.path.abspath(os.path.dirname(__file__))

"""
    MONGO DB Instruction : 
    
    I've while listed all the IPs but just in case connection refused error occurs try this:

    To get it working on your system (Does not work on Sophos Client)
    Step 1 : Go to https://cloud.mongodb.com/v2#/account
    Step 2 : Login via U : "imsleepx@gmail.com", P : "farmer-portal"
    Step 3 : Go to connect and white list your IP address
"""

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    MONGODB_URL = 'mongodb+srv://rohit:rohit@cluster0-ixzb5.mongodb.net/test?retryWrites=true&w=majority'


class DevelopmentConfig(Config):
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
