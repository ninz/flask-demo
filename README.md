flask-demo
==========

Flask Demo for ConFoo 2014

Running hello_world demo:
-------------------------

    python hello.py

Running quickndirty:
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

Testing embeds:
---------------

 * https://www.youtube.com/watch?v=9bZkp7q19f0
 * https://www.nfb.ca/film/the-cat-came-back
 * https://www.flickr.com/photos/eythoringi/12642792555/
