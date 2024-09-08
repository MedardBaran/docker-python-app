import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql


DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PRIVATE_IP = os.getenv('DB_PRIVATE_IP')

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type)

def execute(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    nicks = cursor.fetchall()
    cursor.close()
    connection.close()
    return nicks

def get_db_connection():
    return pymysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_PRIVATE_IP,
        port=3306
    )

