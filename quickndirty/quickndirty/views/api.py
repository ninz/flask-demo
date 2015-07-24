import requests
import json
from flask import request, render_template, redirect, url_for, jsonify
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


@app.route('/api/scraps/<int:scrap_id>')
def get():
    pass


@app.route('/api/scraps/', methods=['POST'])
def create():
    pass


@app.route('/api/scraps/<int:scrap_id>', mehthods=['PUT'])
def update():
    pass


@app.route('/api/scraps/<int:scrap_id>', methods=['DELETE'])
def delete():
    pass
