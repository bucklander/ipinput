"""
API server (via Flask) and WSGI entry-point (via Gunicorn) for ipinput.py functions
"""

from flask import Flask, request, jsonify, abort, make_response
import ipinput
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/routetable", methods=['GET'])
def get_routeTable():
    if request.method == "GET":
        resp = ipinput.openRouteTableFile()
    json_result = json.dumps([route_obj.__dict__ for route_obj in resp])
    return json_result

@app.route("/route/<prefix>", methods=['GET'])
def get_route(prefix):
    if request.method == "GET":
        resp = ipinput.routeLookup(prefix)
    json_result = json.dumps([route_obj.__dict__ for route_obj in resp])
    return json_result

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5017')