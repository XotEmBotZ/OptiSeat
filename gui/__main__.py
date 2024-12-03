import streamlit as st
import pandas as pd

st.set_page_config(layout="wide",page_title="OptiSeat",)

if "db" not in st.session_state:
    st.session_state["db"]="Sqlite3"
if "dbConnStr" not in st.session_state:
    st.session_state["dbConnStr"]="./db.sqlite3"

st.title("OptiSeat")
st.caption("A simple and easy software to generate the seating arrangement of students")

instructions,settings=st.tabs(['Instructions(help)','Settings'])

instructions.text("Instructions")
instructions.text("1)Go to Data Page and enter the required data")
instructions.page_link("pages/Data.py",label="Click Here For Data Insertion Page")
instructions.text("2)Go to Algorithm Page and click on Start Processing")
instructions.page_link("pages/Algorithm.py",label="Click Here For Algorithm Page")
instructions.text("3)Download the Xlsx file")

dbSelect=settings.selectbox("Database",['Sqlite3','MySql'],index=0)
settings.text("Connection sting for sqlite3 is the filepath.")
settings.text("Connection sting for mysql is \"user=<username> passwd=<password> host=<host> database=<database>\".")
dbConnStr=settings.text_input("Database Connection String","./db.sqlite3")

settings.text(f"Selected Database:{st.session_state["db"]}")
settings.text(f"Selected Database Connection String:{st.session_state["dbConnStr"]}")

if settings.button("Save Change"):
    st.session_state["db"]=dbSelect
    st.session_state["dbConnStr"]=dbConnStr