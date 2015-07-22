flask-demo
==========

Flask Demo for ConFoo 2014

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

About oEmbed:
-------------
From http://oembed.com/:
> oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a > website to display embedded content (such as photos or videos) when a user posts a link to that resource, without > having to parse the resource directly.

Some providers of oEmbed content include YouTube, Flickr, and NFB.ca (National Film Board of Canada). Quick 'n Dirty is a consumer of oEmbed content.

Content for testing embeds:
---------------
 * https://www.youtube.com/watch?v=sTSA_sWGM44&noredirect=1
 * https://www.youtube.com/watch?v=9bZkp7q19f0
 * https://www.nfb.ca/film/the-cat-came-back
 * https://www.flickr.com/photos/eythoringi/12642792555/
