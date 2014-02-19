flask-demo
==========

Flask Demo for ConFoo 2014

Running hello_world demo:
-------------------------

    python hello.py

Running quickndirty:
--------------------

    ipython
    >>> from quickndirty import init_db
    >>> init_db()
    sqlite3
    sqlite> .schema scrapbook



Design:

- Flask is much smaller/more lightweight than other frameworks e.g. Django, Pyramid
- Flask is not MVC 
- But it is possible to build MTV-like applications (as in Django)
- Flask requires "view functions" (Views), which take a request and return a response. It is hooked up to one or more routes
- Models/database abstraction layer is optional - you may use database access directly if you choose, i.e. with sqlite, drop .sql schema into project and query using plain sql in views.
- If you choose to use models, you can use a DBAL such as SQLAlchemy
- Templates are optional - though useful. Flask uses the Jinja templating engine.


Flask is a thin wrapper around (mainly):
- Werkzeug (WSGI implementation)
- Jinja2
And also
- blinker
- logging (standard library)


Flask comes with:
- Views
- Routing with variable urls and http methods (using Werkzeug - WSGI)
- Templates (using Jinja)
- Request/Response (Werkzeug)
- Sessions/Cookies (Werkzeug)
- Logging
- Context (application and request)
- Signals (using blinker)
- Test client (based on Werkzeug)

Flask does not come with:
- Form library
- Database layer
- Admin interface
- Caching
- Authentication


BUT these can be added via extensions IF you choose
