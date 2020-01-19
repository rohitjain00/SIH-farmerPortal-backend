"""

    I've while listed all the IPs but just in case connection refused error occurs try this:

    To get it working on your system (Does not work on Sophos Client)
    Step 1 : Go to https://cloud.mongodb.com/v2#/account
    Step 2 : Login via U : "imsleepx@gmail.com", P : "farmer-portal"
    Step 3 : Go to connect and white list your IP address
"""
from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb+srv://rohit:rohit@cluster0-ixzb5.mongodb.net/test?retryWrites=true&w=majority")
