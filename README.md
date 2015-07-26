flask-demo
==========

Flask Demo for ConFoo 2014

Basic Setup:
------------

    pip install virtualenv
    virtualenv flask
    source flask/bin/activate
    pip install -r requirements.txt

Running hello_world demo:
-------------------------

    python hello.py

Running quickndirty (tumblr-ish media sharing website):
--------------------

    # set up db
    ipython
    >>> from quickndirty.database import init_db
    >>> init_db()
    # check schema
    sqlite3 /tmp/test.db
    sqlite> .schema scrapbook
    # start app
    python runserver.py
    
Using quickndirty
-----------------
There is a web frontend available at http://127.0.0.1:5000/ in the browser, and an API available at http://127.0.0.1:5000/api. The API can be called with any HTTP client you wish, but the Postman extension for Chrome is a good choice. I've uploaded some example calls here: https://www.getpostman.com/collections/9c65431283ab1d59e34f.

About oEmbed:
-------------
From http://oembed.com/:
> oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a  website to display embedded content (such as photos or videos) when a user posts a link to that resource, without  having to parse the resource directly.

Some providers of oEmbed content include YouTube, Flickr, and NFB.ca (National Film Board of Canada). Quick 'n Dirty is a consumer of oEmbed content.

Content for testing embeds:
---------------
 * https://www.youtube.com/watch?v=sTSA_sWGM44&noredirect=1
 * https://www.youtube.com/watch?v=9bZkp7q19f0
 * https://www.nfb.ca/film/the-cat-came-back
 * https://www.flickr.com/photos/eythoringi/12642792555/
