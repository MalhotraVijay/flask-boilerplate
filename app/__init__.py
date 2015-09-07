from flask import Flask
import os

from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

environment = os.environ.get('prod_env','development')

""" Setting up the environment"""

if environment == 'production':
	app.config.from_object('conf.mainconf.ProductionConfig') 
else:
	app.config.from_object('conf.mainconf.DevelopmentConfig')


""" Initiating the logger"""
logger = app.logger 
logger.setLevel('DEBUG')



"""Set the app secret to use sessions """
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from api import outlets
