#Main configuration file for the complete flask application

from flask import Config

""" Common config can go here """


class DevelopmentConfig(Config):
    MONGODB_DATABASE = 'db_name'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'username'
    MONGODB_PASSWORD = 'password'



class ProductionConfig(Config):
    MONGODB_DATABASE = 'db_name'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'username'
    MONGODB_PASSWORD = 'password'
