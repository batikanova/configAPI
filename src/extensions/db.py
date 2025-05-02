from psycopg2 import pool
import sys



dbPool = pool.SimpleConnectionPool(
    minconn=1,       
    maxconn=10,       
    dbname="postgres",
    user="postgres",
    password="workpalas",
    host="localhost",
    port="5433"
)

def dbConn():
    try:
        conn = dbPool.getconn()
        return conn
    except Exception as e:
        print("Error getting connection from pool:", str(e))
        return None


def returnConn(conn):
    try:
        dbPool.putconn(conn)
    except Exception as e:
        print("Error returning connection to pool:", str(e))

        
def closePool():
    try:
        dbPool.closeall()
    except Exception as e:
        print("Error closing connection pool:", str(e))
