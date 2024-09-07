import logging
import random
from db import pool
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_random_nick():
    with pool.connect() as db_conn:
        nicks = db_conn.execute("SELECT * FROM nicks")

    return random.choice(nicks)


@app.route('/')
def hello():
    nick = get_random_nick()
    return ('Hello Cloud!\n'
            'This app was created for GCP Application Development Challenge\n')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
