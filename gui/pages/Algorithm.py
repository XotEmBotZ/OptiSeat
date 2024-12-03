import streamlit as st
from main import algo
import streamlit as st
from connections import sqlite3Connector,mySqlConnector
from utils import utils

if "db" not in st.session_state:
    st.session_state["db"]="Sqlite3"
if "dbConnStr" not in st.session_state:
    st.session_state["dbConnStr"]="./db.sqlite3"

try:
    conn=sqlite3Connector(connection_name="sqlite3",database="./test.sqlite3")
    if st.session_state["db"]=="Sqlite3":
        conn=sqlite3Connector(connection_name="sqlite3",database=st.session_state["dbConnStr"])
    elif st.session_state["db"]=="MySql":
        config=utils.mysqlConnectionStringToDict(st.session_state["dbConnStr"])
        conn=mySqlConnector(connection_name="mysql",**config)

    def handleProcessing():
        res=algo.allocateSeat(conn)
        postRes=algo.postProcessRes(res)
        workbook=utils.getXlsxFile(postRes,"data.xlsx")
        st.download_button(label="Download file",data=workbook,file_name="studentSeatAllocation.xlsx")  # type: ignore

    if st.sidebar.button("Start Processing"):
        handleProcessing()

except Exception as e:
    st.error(e)