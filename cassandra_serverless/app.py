import json
import random
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def lambda_handler(event, context):
    hash = event['hash']
    return handle_get(hash)


def handle_get(hash):
    url = get_url(hash)
    target_location = "http://shorty.elpalomito.io"
    if url != "none":
        target_location = url
    print(f'[{hash}] redirected to [{target_location}]')
    return {
        "statusCode": 301,
        "headers": {
            "Location": target_location
        },
    }


def handle_post(url):
    result = post_url(url)
    status = 400
    if isinstance(result, str):
        status = 200
    return {
        "statusCode": status,
        "body": json.dumps({
            "Message": result
        }),
    }


def post_url(url):
    hash = _get_key()
    session = _get_session()
    try:
        session.execute('INSERT INTO mapping (search_hash, url) VALUES (%s, %s)', [hash, url])
        return hash
    except Exception as ex:
        return ex


def get_url(hash):
    session = _get_session()
    try:
        row = session.execute('SELECT * FROM mapping where search_hash=%s', [hash])[0]
        return row.url
    except IndexError:
        return "none"


def _get_session():
    auth_provider = PlainTextAuthProvider(username='', password='')
    cluster = Cluster([''], port=9042, auth_provider=auth_provider)
    return cluster.connect('shortener')


def _get_key():
    allowed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowed_list = list(allowed)
    random.shuffle(allowed_list)
    shuffled = ''.join(allowed_list)
    return shuffled[0:7]
