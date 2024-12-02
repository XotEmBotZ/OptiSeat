import streamlit as st
from main import algo
import streamlit as st
from connections import sqlite3Connector
from utils import utils

try:
    conn=sqlite3Connector(connection_name="sqlite3",database="./test.sqlite3")

    def handleProcessing():
        res=algo.allocateSeat(conn)
        postRes=algo.postProcessRes(res)
        workbook=utils.getXlsxFile(postRes,"data.xlsx")
        st.download_button(label="Download file",data=workbook,file_name="studentSeatAllocation.xlsx")  # type: ignore

    if st.sidebar.button("Start Processing"):
        handleProcessing()

except Exception as e:
    st.error(e)