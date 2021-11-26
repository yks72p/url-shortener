import os
from flask import Flask, make_response, jsonify

from rest_api import url_utils
from rest_api.api_impl import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        CASSANDRA_ENDPOINTS=[os.environ.get('CASSANDRA_ENDPOINT', 'cassandra')],
        CASSANDRA_KEYSPACE='url_shortener',
        SHORT_URL_PREFIX="http://localhost:5000/",
        INSTANCE_ID=1,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)
    url_utils.cache.clear()
    app.register_blueprint(api)

    if app.config['INSTANCE_ID'] > url_utils.INSTANCE_ID_MASK:
        raise Exception("Instance id can't be more than {}".format(url_utils.INSTANCE_ID_MASK))

    return app
