import logging
import random
import sqlalchemy
import db

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    with db.pool.connect() as db_conn:
        nicks = db_conn.execute(sqlalchemy.text("SELECT * FROM nicks")).fetchall()

    nick = random.choice(nicks)
    return (f'Hello {nick}!\n'
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
