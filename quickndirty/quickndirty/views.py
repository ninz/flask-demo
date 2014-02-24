import requests
import json
from flask import request, render_template, redirect, url_for, jsonify
from quickndirty import app
from quickndirty.database import db_session
from quickndirty.models import Scrapbook
from pyembed.core import discovery


@app.route('/')
def show_entries():
    entries = db_session.query(Scrapbook).all()
    return render_template('show_entries.html', entries=entries)


@app.route('/new')
def new_entry():
    return render_template('new_entry.html')


@app.route('/create', methods=["POST"])
def add_entry():
    s = Scrapbook(
        request.form['content_url'],
        request.form['title'],
        resource_type=request.form['resource_type'],
        version=request.form['version'],
        author_name=request.form['author_name'],
        author_url=request.form['author_url'],
        provider_name=request.form['provider_name'],
        provider_url=request.form['provider_url'],
        thumbnail_url=request.form['thumbnail_url'],
        thumbnail_width=request.form['thumbnail_width'],
        thumbnail_height=request.form['thumbnail_height'],
        url=request.form['url'],
        html=request.form['html'],
        width=request.form['width'],
        height=request.form['height']
    )
    db_session.add(s)
    db_session.commit()
    #flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/lookup', methods=["POST"])
def lookup_oembed():
    content_url = request.form.get('content_url')
    (discovered_format, oembed_url) = discovery.get_oembed_url(
        content_url, max_width=300, max_height=300)
    response = requests.get(oembed_url)
    oembed_fields = json.loads(response.text)
    return jsonify(oembed_fields)