import datetime

import importlib.resources
from utils.types import RawStudentType, RoomType, StudentType, Timetable
from utils import utils

def createSchema(conn) -> None:
    cursor = conn.cursor()
    query = open(str(importlib.resources.files("sql") / "schema.sql")).read()
    query = query.split(';')
    for q in query:
        cursor.execute(q)
    conn.commit()


def checkSchema(conn) -> None:
    ...


# DO THE CHECKING IN THE FUNCTION ALSO
# like (for ef in std) as per the database schema -> assert len(sec)=1 , "Length of sec is not 1"


def insertRoom(conn, name: str, noBench: int, benchStd: int = 2) -> int:
    cursor = conn.cursor()
    assert len(name) <= 5, "Length of sec name is more than 5"
    query = f"INSERT INTO room (name,num_benches,bench_stud) VALUES ('{
        name}',{noBench},{benchStd}) returning id;"
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertTeacher(conn, name: str,) -> int:
    query = f"INSERT INTO teacher (name) VALUES ('{name}') returning id;"
    cursor = conn.cursor()
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertStudent(conn, std: int, sec: str, sub: str, isSeq: bool, rollStart: int = 0, rollEnd: int = 0, rollArr: tuple[int,...] | None = None,) -> int:
    cursor = conn.cursor()
    assert len(sec) == 1, 'Length of sec is not 1'
    assert len(sub) == 3, 'Length of sub is not 3'
    if isSeq == True:
        query = f"INSERT INTO student (std,sec,sub,is_seq,roll_start,roll_end) values ({
            std},'{sec}','{sub}',{isSeq},{rollStart},{rollEnd}) returning id;"
    else:
        assert rollArr is not None, 'Roll array is None'
        assert not len(rollArr) == 0, 'Length of roll array is 0'
        query = f"INSERT INTO student (std,sec,sub,is_seq,roll_arr) values ({std},'{
            sec}','{sub}',{isSeq},'{utils.cvtLstIntToSql(rollArr)}') returning id;"
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertTimetable(conn,date:datetime.date,std:int,sub:str)->int:
    cur=conn.cursor()
    query=f"INSERT INTO timetable(date,std,sub) VALUES ('{date.strftime("%Y-%m-%d")}',{std},'{sub}') RETURNING ID"
    cur.execute(query)
    id=cur.fetchone()[0]
    conn.commit()
    return id

def fetchRooms(conn)->list[RoomType]:
    cur=conn.cursor()
    query="SELECT name,num_benches,bench_stud FROM room;"
    cur.execute(query)
    opt=cur.fetchall()
    res:list[RoomType]=[{"name":row[0],"numBench":row[1],"benchStud":row[2]} for row in opt]
    return res

def fetchStud(conn,std:int,sub:str)->list[StudentType]:
    cur=conn.cursor()
    query=f"SELECT std,sub,sec,is_seq,roll_start,roll_end,roll_arr FROM student WHERE std={std} AND sub= '{sub}' ORDER BY sec"
    cur.execute(query)
    opt=cur.fetchall()
    res=[]
    for studRow in opt:
        studDict={
            "std":studRow[0],
            "sub":studRow[1],
            "sec":studRow[2],
        }
        # "isSeq":studRow[3],
        # "rollStart":studRow[4],
        # "rollEnd":studRow[5],
        # "rollArr":studRow[6],
        if studRow[3]:
            res.extend([{**studDict,"rollNo":roll} for roll in range(studRow[4],studRow[5]+1)])
        else:
            rollArr=eval(studRow[6])
            res.extend([{**studDict,"rollNo":roll} for roll in rollArr])
    return res

def fetchStudRaw(conn)->list[RawStudentType]:
    cur=conn.cursor()
    cur.execute("SELECT std,sec,sub,is_seq,roll_start,roll_end,roll_arr FROM student")
    opt=cur.fetchall()
    res:list[RawStudentType]=[{"std":row[0],"sec":row[1],"sub":row[2],"isSeq":row[3],"rollStart":row[4],"rollEnd":row[5],"rollArr":eval(row[6]) if row[6] is not None else None} for row in opt]  # type: ignore
    return res

def fetchTimetable(conn)->list[Timetable]:
    cur=conn.cursor()
    cur.execute("SELECT date,std,sub FROM timetable;")
    opt=cur.fetchall()
    res:list[Timetable]=[{
        "date":datetime.datetime.strptime(row[0],"%Y-%m-%d").date(),
        "std":row[1],
        "sub":row[2]
        } for row in opt]  # type: ignore
    conn.commit()
    return res

def fetchDistinctDate(conn) -> list[datetime.date]:
    cursor = conn.cursor()
    query="SELECT DISTINCT(date) FROM timetable;"
    cursor.execute(query)
    res=cursor.fetchall()
    return [datetime.datetime.strptime(date[0],"%Y-%m-%d").date() for date in res]


def fetchStdSub(conn, date: datetime.date) -> list[tuple[int, str]]:
    cursor = conn.cursor()
    query=f"SELECT std,sub FROM timetable WHERE date='{date.strftime("%Y-%m-%d")}' ORDER BY std,sub ASC"
    cursor.execute(query)
    res:list[tuple[int,str]]=cursor.fetchall()
    return res

def deleteAllRooms(conn) -> None:
    cur=conn.cursor()
    cur.execute("DELETE FROM room;")
    conn.commit()

def deleteAllStudent(conn)->None:
    cur=conn.cursor()
    cur.execute("DELETE FROM student;")
    conn.commit()

def deleteAllTimeTable(conn)->None:
    cur=conn.cursor()
    cur.execute("DELETE FROM timetable;")
    conn.commit()

if __name__ == "__main__":
    import mysql.connector as mys
    import sqlite3
    import pandas as pd
    conn = sqlite3.connect("test.sqlite3")

    createSchema(conn)
    insertStudent(conn,12,"A","Eng",True,1,44)
    insertStudent(conn,12,"B","Eng",False,rollArr=(23,23,2,32,3))
    print(pd.DataFrame(fetchStudRaw(conn)))
