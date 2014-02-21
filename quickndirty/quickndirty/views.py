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


@app.route('/add', methods=["POST"])
def add_entry():
    s = Scrapbook(
        request.form['content_url'],
        request.form['title'],
        request.form['resource_type'],
        request.form['version'],
        request.form['author_name'],
        request.form['author_url'],
        request.form['provider_name'],
        request.form['provider_url'],
        request.form['thumbnail_url'],
        request.form['thumbnail_width'],
        request.form['thumbnail_height'],
        request.form['url'],
        request.form['width'],
        request.form['height']
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