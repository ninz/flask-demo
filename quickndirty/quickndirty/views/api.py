import requests
import json
from flask import request, jsonify
from quickndirty import app
from quickndirty.database import db_session
from quickndirty.models import Scrapbook
from pyembed.core import discovery


@app.route('/api')
def index():
    pass


@app.route('/api/scraps')
def get_all():
    scraps = db_session.query(Scrapbook).all()
    return jsonify({'scraps' : [scrap.as_dict() for scrap in scraps]})


@app.route('/api/scraps/<int:scrap_id>')
def get(scrap_id):
    scrap = db_session.query(Scrapbook).get(scrap_id)
    if not scrap:
        return error("Scrap not found")
    return jsonify(scrap.as_dict())


@app.route('/api/scraps/', methods=['POST'])
def create():
    # if not request.json or not 'name' in request.json:
    #         abort(400)
    #     dev = Developer(request.json.name, request.json.get('hireDate', ''), request.json.get('focus',''))
    #     db.session.add(dev)
    #     db.session.commit()
    #     return jsonify( { 'developer': dev } ), 201
    pass


@app.route('/api/scraps/<int:scrap_id>', methods=['PUT'])
def update():
    pass


@app.route('/api/scraps/<int:scrap_id>', methods=['DELETE'])
def delete():
    pass


def error(error_message="Resource not found", status_code=404):
    resp = jsonify(status_code=status_code, error_message=error_message)
    resp.status_code = status_code
    return resp