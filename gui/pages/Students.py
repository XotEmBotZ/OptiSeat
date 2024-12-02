import sys
import pathlib
import streamlit as st
from connections import sqlite3Connector


conn=sqlite3Connector(connection_name="sqlite3",database="./test.sqlite3")
st.text(conn.cursor().execute("SELECT * FROM room"))
