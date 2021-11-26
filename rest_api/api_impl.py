import json
from datetime import timedelta, date
from flask import request, Blueprint, abort, current_app

from rest_api import db, url_utils

api = Blueprint("api", __name__)


@api.route('/createURL', methods=['POST'])
def create_url():
    contents = request.get_json()
    if not request.json or not 'original_url' in request.json:
        abort(400)
    original_url = contents['original_url']

    short_id = url_utils.get_a_new_id()
    db.upsert_short_url(short_id, original_url)
    response = {"short_link": "{}/getURL/{}".format(current_app.config['SHORT_URL_PREFIX'], url_utils.encode_short_id(short_id)),
                'original_url': original_url, 'expire_date': str(date.today() + timedelta(days=30))}
    return json.dumps(response)


@api.route('/getURL/<string:url_hash>', methods=['GET'])
def get_url(url_hash):
    # stub = "https://some-stub-url-used-for-debug-purpose.by"
    # return stub

    original_url = db.get_original_url(url_utils.decode_short_id(url_hash))
    if original_url is None:
        return abort(404)
    else:
        return original_url