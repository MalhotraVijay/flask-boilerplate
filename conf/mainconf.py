#Main configuration file for the complete flask application

from flask import Config

""" Common config can go here """


class DevelopmentConfig(Config):
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''
