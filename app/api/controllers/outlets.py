from flask import Flask,jsonify,Response
from flask_restful import Resource, Api

import json
from bson import json_util

from app import app

api = Api(app)

class AppInitResource(Resource):
        def get(self):
            return Response(json.dumps({
                'app_name': 'Flask-Boilerplate' ,
                'version':'v0.0.1',
                'routes' : '/routes'
                }),mimetype="application/json")



class OutletList(Resource):
    def get(self):
    	outlets = ["outlet1","outlet2","outlet3"]
    	response = json.dumps({'outlets' : outlets},default=json_util.default)
        return Response(response,mimetype="application/json")


class SingleOutlet(Resource):
    def get(self,outletId):
        if int(outletId) > 3 or int(outletId) <= 0:
            return Response(json.dumps({'status' : False, 
                'message' : 'No outlet found, invalid ID'}),mimetype="application/json")

        outlets = ["outlet1","outlet2","outlet3"]
        response = json.dumps({'outlet' : outlets[int(outletId)-1]},default=json_util.default)
        return Response(response,mimetype="application/json")



api.add_resource(AppInitResource, '/')
api.add_resource(OutletList, '/outlets')
api.add_resource(SingleOutlet, '/outlet/<outletId>')
