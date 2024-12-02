import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))


import sqlite3
from streamlit.connections import BaseConnection
from streamlit import cache_data
from sql.func import checkSchema, createSchema,insertRooms

class sqlite3Connector(BaseConnection):
    def _connect(self, **kwargs) -> sqlite3.Connection:
        conn: sqlite3.Connection = sqlite3.connect(**kwargs)
        createSchema(conn)
        insertRooms(conn,"XIC",23,2)
        insertRooms(conn,"XIA",21,2)
        insertRooms(conn,"XIB",22,2)
        insertRooms(conn,"XID",24,2)
        return conn
    
    def cursor(self)->sqlite3.Cursor:
        return self._instance.cursor()