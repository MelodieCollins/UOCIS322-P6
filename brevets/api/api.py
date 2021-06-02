# Streaming Service

import os
import itertools
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import json
#from string import letters, digits

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

class listAll(Resource):
	def get(self, dtype='json'):
		items = list(db.tododb.find())
		top = int(request.args.get('top', default='-1').strip())
		open_close = []
		for i in items:
			tmp = [str(i['open']), str(i['close'])]
			open_close.append(tmp)

		if dtype == 'csv':
			return open_close
		x = {
			"List All": open_close
		}
		y = json.dumps(x)
		return y

class listOpenOnly(Resource):
	def get(self, dtype='json'):
		items = list(db.tododb.find())
		top = int(request.args.get('top', default='-1').strip())
		
		#openlist = []
		#for i in items:
			#openlist.append(str(i['open']))

		open_only = []
		app.logger.debug(top)
		if top != -1:
			#ascending = openlist.sort()
			#app.logger.debug(ascending)
			for i in items:
				if len(open_only) < int(top):
					open_only.append(str(i['open']))
		else:
			for i in items:
				open_only.append(str(i['open']))

		if dtype == 'csv':
			return open_only
		x = {
			"List Open Only": open_only
		}
		y = json.dumps(x)
		return y

class listCloseOnly(Resource):
	def get(self, dtype='json'):
		items = list(db.tododb.find())
		top = int(request.args.get('top', default='-1').strip())
		#closelist = []
		#for i in items:
			#closelist.append(str(i['close']))
		#ascending = sorted(closelist, key=alphanumeric_key)

		close_only = []
		app.logger.debug(top)
		if top != -1:
			#ascending = closelist.sort()
			for i in items:
				if len(close_only) < int(top):
					close_only.append(str(i['close']))
		else:
			for i in items:
				close_only.append(str(i['close']))

		if dtype == 'csv':
			return close_only
		x = {
			"List Close Only": close_only
		}
		y = json.dumps(x)
		return y

api.add_resource(listAll, '/listAll/', '/listAll/<dtype>')
api.add_resource(listOpenOnly, '/listOpenOnly/', '/listOpenOnly/<dtype>')
api.add_resource(listCloseOnly, '/listCloseOnly/', '/listCloseOnly/<dtype>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)