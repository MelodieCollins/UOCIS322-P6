# Streaming Service

import os
import itertools
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import json

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

class listAll(Resource):
	def get(self, dtype, top):
		items = list(db.tododb.find())
		open_close = []
		for i in items:
			tmp = [str(i['open']), str(i['close'])]
			open_close.append(tmp)

		topk = top
		if dtype == 'CSV':
			# open_close is a list of lists (make into list? ->merged)
			return open_close
		x = {
			"List All": open_close
		}
		y = json.dumps(x)
		return y

class listOpenOnly(Resource):
	def get(self, dtype, top):
		items = list(db.tododb.find())
		#openlist = []
		#for i in items:
			#openlist.append(str(i['open']))
		res_open = [ sub['open'] for sub in items ]
		open_only = ",".join(res_open) + "\n"
		open_only = open_only[:-1]

		topk = top
		if dtype == 'CSV':
			return open_only
		# return json format
		x = {
			"List Open Only": open_only
		}
		y = json.dumps(x)
		return y

class listCloseOnly(Resource):
	def get(self, dtype, top):
		items = list(db.tododb.find())
		res_close = [ sub['close'] for sub in items ]
		close_only = ",".join(res_close) + "\n"
		close_only = close_only[:-1]

		topk = top
		if dtype == 'CSV':
			return close_only
		x = {
			"List Close Only": close_only
		}
		y = json.dumps(x)
		return y

api.add_resource(listAll, '/listAll/<dtype><top>')
api.add_resource(listOpenOnly, '/listOpenOnly/<dtype><top>')
api.add_resource(listCloseOnly, '/listCloseOnly/<dtype><top>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)