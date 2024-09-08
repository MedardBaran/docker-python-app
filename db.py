import os
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy


INSTANCE_CONNECTION_NAME = os.environ['DB_CONNECTION_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type)

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
