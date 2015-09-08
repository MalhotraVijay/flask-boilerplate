from flask import Flask
from flask_restful import Resource, Api

from app import app

api = Api(app)

class AppInitResource(Resource):
        def get(self):
            return {'appName': 'Tweeny' ,'version':'v0.0.1'}



class OutletList(Resource):
    def get(self):
        return {'outletList' : ['1','2','3'] }


api.add_resource(AppInitResource, '/')
api.add_resource(OutletList, '/outlets')
