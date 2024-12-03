import pandas as pd
import streamlit as st
from connections import sqlite3Connector,mySqlConnector
from sql import func
from utils import utils
from utils.types import RawStudentType
import datetime

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

    st.header("Modify the data")
    st.caption("Use the Demo Entries to get the datatype and fill similarly")
    st.caption("Use Commit Changes to push the changes to database")
    st.caption("Use Refresh to repull data from the database")

    tt,rm,stud=st.tabs(['Timetable',"Room","Students(Raw)"])

    ttDf=pd.DataFrame(func.fetchTimetable(conn),columns=["date","std","sub"])
    finalTtDf=ttDf.copy()
    finalTtDf["date"]=pd.to_datetime(finalTtDf["date"]).dt.strftime("%Y-%m-%d")
    editedTtDf: pd.DataFrame=tt.data_editor(finalTtDf,use_container_width=True,num_rows="dynamic",key="ttDf")

    roomDf=pd.DataFrame(func.fetchRooms(conn),columns=["name","numBench","benchStud"])
    editedRoomDf: pd.DataFrame= rm.data_editor(roomDf,use_container_width=True,num_rows="dynamic",key="roomDf")

    stdData: list[RawStudentType]=func.fetchStudRaw(conn)
    finalStdData=[{
        "std":std["std"],
        "sec":std["sec"],
        "sub":std["sub"],
        "isSeq":std["isSeq"],
        "rollStart":std["rollStart"],
        "rollEnd":std["rollEnd"],
        "rollArr":str(std["rollArr"]) if std["rollArr"] else None,
    } for std in stdData]
    studDf=pd.DataFrame(finalStdData,columns=["std","sec","sub","isSeq","rollStart","rollEnd","rollArr"])
    editedStudDf: pd.DataFrame=stud.data_editor(studDf,use_container_width=True,num_rows="dynamic",key="studDf")




    if st.sidebar.button("Commmit Changes"):
        func.deleteAllTimeTable(conn)
        editedTtDf["date"]=pd.to_datetime(editedTtDf["date"]).dt.date
        utils.insertManyTimetable(conn,editedTtDf.to_dict("records"))  # type: ignore

        func.deleteAllRooms(conn)
        utils.insertManyRooms(conn,editedRoomDf.to_dict("records"))  # type: ignore

        func.deleteAllStudent(conn)
        df=editedStudDf.copy()
        df["rollArr"]=df["rollArr"].apply(lambda x:eval(str(x)))
        utils.insertManyStuds(conn,df.to_dict("records"))  # type: ignore

        st.success("Commit Done")

    if st.sidebar.button("Refresh"):
        st.sidebar.text("IN RERUN")
        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("Insert Demo Entry"):
        func.insertTimetable(conn,datetime.date.today(),12,"phy")

        func.insertRoom(conn,"XIIA",23,2)

        func.insertStudent(conn,1,"A","eng",True,1,2)
        func.insertStudent(conn,1,"A","eng",False,rollArr=(23,45,67,))
        st.rerun()

except Exception as e:
    st.error(e)