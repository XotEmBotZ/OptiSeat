import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))


import sqlite3
from streamlit.connections import BaseConnection
from streamlit import cache_data
from sql.func import checkSchema, createSchema
import mysql.connector as msqlconn

class sqlite3Connector(BaseConnection):
    def _connect(self, **kwargs) -> sqlite3.Connection:
        conn: sqlite3.Connection = sqlite3.connect(**kwargs)
        createSchema(conn)
        # insertRooms(conn,"XIA",23)
        return conn
    
    def cursor(self)->sqlite3.Cursor:
        return self._instance.cursor()
    
    def commit(self)->None:
        self._instance.commit()

class mySqlConnector(BaseConnection):
    def _connect(self, **kwargs):
        conn = msqlconn.connect(**kwargs)
        createSchema(conn)
        # insertRooms(conn,"XIA",23)
        return conn
    
    def cursor(self)->sqlite3.Cursor:
        return self._instance.cursor()
    
    def commit(self)->None:
        self._instance.commit()