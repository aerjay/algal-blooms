import flask
import json
from flask import request, jsonify, render_template

app = flask.Flask(__name__, static_url_path='', static_folder='./www')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v0/ratios', methods=['GET'])
def api_id():
    query_parameters = request.args

    longitude = query_parameters.get('lon')
    latitude = query_parameters.get('lat')

    # Let's return the tile containing Chicago, IL
    if longitude == "-81.769110" and latitude == "42.124753":
        # Hard-coded values for now, need to store this in a database
        with open('ratios.json') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    else:
        return jsonify("No ratios found.")

app.run()