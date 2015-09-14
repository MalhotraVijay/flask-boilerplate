from flask import Flask,jsonify,Response
from flask_restful import Resource, Api

import json
from bson import json_util

from app import app, db

api = Api(app)

class AppInitResource(Resource):
        def get(self):
            return {'appName': 'Tweeny' ,'version':'v0.0.1'}



class OutletList(Resource):
    def get(self):
    	outlets = db.outlets.find()
    	outlets = list(outlets)
    	response = json.dumps({'outlets' : outlets},default=json_util.default)
        return Response(response,mimetype="application/json")


class SingleOutlet(Resource):
	def get(self,outletId):
		print outletId
		#outlets = db.outlets.get_from_id(outletId)
		#print outlets
		return {'done' : '1'}



api.add_resource(AppInitResource, '/')
api.add_resource(OutletList, '/outlets')
api.add_resource(SingleOutlet, '/outlets/<outletId>')
