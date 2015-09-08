from flask import Flask
import os

from werkzeug.contrib.fixers import ProxyFix
from flask.ext.mongokit import MongoKit 


app = Flask(__name__)

environment = os.environ.get('prod_env','development')

""" Setting up the environment from the mainconf """

if environment == 'production':
	app.config.from_object('conf.mainconf.ProductionConfig') 
else:
	app.config.from_object('conf.mainconf.DevelopmentConfig')


""" Initiating the logger"""
logger = app.logger 
logger.setLevel('DEBUG')


""" Initiating mongodb db object """
db = MongoKit(app)

print db

"""Set the app secret to use sessions """
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from api.controllers import outlets
