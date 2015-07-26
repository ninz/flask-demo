import requests
import json
from flask import request, jsonify, url_for
from quickndirty import app
from quickndirty.database import db_session
from quickndirty.models import Scrapbook
from pyembed.core.discovery import PyEmbedDiscoveryError, get_oembed_url


@app.route('/api')
def index():
    return jsonify({'scraps': url_for('get_all')})


@app.route('/api/scraps')
def get_all():
    scraps = db_session.query(Scrapbook).all()
    return jsonify({'scraps': [scrap.as_dict() for scrap in scraps]})


@app.route('/api/scraps', methods=['POST'])
def create():
    json_data = request.get_json(force=True)
    try:
        (discovered_format, oembed_url) = get_oembed_url(json_data['scrap'], max_width=300, max_height=300)
    except PyEmbedDiscoveryError:
        return error("Invalid oEmbed resource URL", 400)
    except KeyError:
        return error("POST to /api/scraps takes one parameter, scrap", 400)

    response = requests.get(oembed_url)
    oembed_fields = json.loads(response.text)
    s = Scrapbook(json_data['scrap'], **oembed_fields)
    db_session.add(s)
    db_session.commit()
    return jsonify({"scrap": url_for('get', **{'scrap_id': s.id})}), 201


@app.route('/api/scraps/<int:scrap_id>')
def get(scrap_id):
    scrap = db_session.query(Scrapbook).get(scrap_id)
    if not scrap:
        return error("Scrap not found")
    return jsonify(scrap.as_dict())


@app.route('/api/scraps/<int:scrap_id>', methods=['DELETE'])
def delete(scrap_id):
    s = db_session.query(Scrapbook).get(scrap_id)
    uri = None
    if not s:
        return error("Scrap not found")
    else:
        uri = url_for('get', **{'scrap_id': s.id})
    db_session.delete(s)
    db_session.commit()
    return jsonify({"message": "%s was successfully deleted" % uri})


def error(error_message="Resource not found", status_code=404):
    resp = jsonify(status_code=status_code, error_message=error_message)
    resp.status_code = status_code
    return resp
