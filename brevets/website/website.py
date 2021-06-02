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
    dtype = request.args.get('json_or_csv', default='json')
    top = request.args.get('top').strip()
    url = 'http://restapi:5000/listAll/' + dtype
    if top != "":
        try:
            top=int(top)
        except ValueError as verr:
            abort(400, str(verr))
        url += f"?top={top}"
    r = requests.get(url)
    return flask.jsonify({"result": r.text})

@app.route('/listOpenOnly')
def listOpenOnly():
    dtype = request.args.get('json_or_csv', default='json')
    top = request.args.get('top').strip()
    url = 'http://restapi:5000/listOpenOnly/' + dtype
    if top != "":
        try:
            top=int(top)
        except ValueError as verr:
            abort(400, str(verr))
        url += f"?top={top}"
    r = requests.get(url)
    app.logger.debug(r)
    return flask.jsonify({"result": r.text})

@app.route('/listCloseOnly')
def listCloseOnly():
    dtype = request.args.get('json_or_csv', default='json')
    top = request.args.get('top').strip()
    url = 'http://restapi:5000/listCloseOnly/' + dtype
    if top != "":
        try:
            top=int(top)
        except ValueError as verr:
            abort(400, str(verr))
        url += f"?top={top}"
    r = requests.get(url)
    return flask.jsonify({"result": r.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)