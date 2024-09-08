import logging
import random
import sqlalchemy
import db_utils

from flask import Flask, request, jsonify
from sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = db_utils.get_connection_str()
db = SQLAlchemy(app)

@app.route('/')
def hello():
    nicks = get_nicks_from_db()

    nick = random.choice(nicks)
    return (f'Hello {nick}!\n'
             'This app was created for GCP Application Development Challenge\n')


def get_nicks_from_db():
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM nicks")  # Replace 'your_table_name' with your actual table name
    nicks = cursor.fetchall()
    cursor.close()
    connection.close()
    return nicks


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
