#Main configuration file for the complete flask application

from flask import Config

""" Common config can go here """


class DevelopmentConfig(Config):
    MONGODB_DATABASE = 'tweenyapp'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'tweeny'
    MONGODB_PASSWORD = 'tweeny02'


