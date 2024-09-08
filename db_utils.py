import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql


INSTANCE_CONNECTION_NAME = os.getenv('DB_CONNECTION_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type)


def get_connection_str():
    return f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_socket=/cloudsql/{INSTANCE_CONNECTION_NAME}'


def get_db_connection():
    return pymysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        unix_socket=f'/cloudsql/{INSTANCE_CONNECTION_NAME}'
    )

