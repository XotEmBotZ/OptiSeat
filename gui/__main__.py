import streamlit as st
import pandas as pd

st.set_page_config(layout="wide",page_title="Index")

st.title("OptiSeat")
st.caption("A simple and easy software to generate the seating arrangement of students")
st.divider()

st.text("Instructions")
st.text("1)Go to Data Page and enter the required data")
st.page_link("pages/Data.py",label="Data Insertion Page")
st.text("2)Go to Algorithm Page and click on Start Processing")
st.page_link("pages/Algorithm.py",label="Algorithm Page")
st.text("3)Download the Xlsx file")