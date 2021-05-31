# add html with three buttons (list all, list open only, list close only), 
# one text box for top value
# one check box for csv vs json (error if both checked, default to json if non checked)

# when someone clicks buttons, send request back to
# a route that you're handling in flask.
# Then, using built-in requests package, send manual get request to your restapi 

from flask import Flask, render_template, request
import flask
import requests
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/listAll')
def listAll():
	dtype = request.args.get('json_or_csv', default='JSON')
	# top = request.args.get('top', default=-1)
	r = requests.get('http://restapi:5000/listAll/' + dtype)
	return flask.jsonify({"result": r.text})

@app.route('/listOpenOnly')
def listOpenOnly():
	#get json_or_csv
	dtype = request.args.get('json_or_csv', default='JSON')
	r = requests.get('http://restapi:5000/listOpenOnly/' + dtype)
	app.logger.debug(r)
	return flask.jsonify({"result": r.text})

@app.route('/listCloseOnly')
def listCloseOnly():
	dtype = request.args.get('json_or_csv', default='JSON')
	r = requests.get('http://restapi:5000/listCloseOnly/' + dtype)
	return flask.jsonify({"result": r.text})

# Run the application
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)