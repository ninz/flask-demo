from flask import Flask
from quickndirty.database import db_session
#import flask_raptor

app = Flask(__name__)
#flask_raptor.init_app(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import quickndirty.views
