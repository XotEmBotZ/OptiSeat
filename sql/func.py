import datetime
import importlib.resources
from utils.types import RoomType, studentType
from utils.utils import cvtLstIntToSql

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


def insertRooms(conn, name: str, noBench: int, benchStd: int = 2) -> int:
    cursor = conn.cursor()
    assert len(name) <= 5, "Length of sec name is more than 5"
    query = f"INSERT INTO room (name,num_benches,bench_stud) VALUES ('{
        name}',{noBench},{benchStd}) returning id;"
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertTeachers(conn, name: str,) -> int:
    query = f"INSERT INTO teacher (name) VALUES ('{name}') returning id;"
    cursor = conn.cursor()
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertStudents(conn, std: int, sec: str, sub: str, isSeq: bool, rollStart: int = 0, rollEnd: int = 0, rollArr: list[int] | None = None,) -> int:
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
            sec}','{sub}',{isSeq},'{cvtLstIntToSql(rollArr)}') returning id;"
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def insertTimetable(conn, date: datetime.date, std: int, sub: str) -> int:
    cursor = conn.cursor()
    assert len(sub) == 3, 'Length of sub is not 3'
    query = f'''INSERT INTO timetable (date,std,sub) VALUES ('{
        date.strftime("%Y-%m-%d")}',{std},'{sub}') returning id;'''
    cursor.execute(query)
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def fetchRooms(conn) -> list[RoomType]:
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    return []


def fetchStud(conn, std: int, sub: str) -> list[studentType]:
    # [{std:23,sub:"eng",roll:1},{std:23,sub:"eng",roll:2},{std:23,sub:"eng",roll:3},{std:23,sub:"eng",roll:4}]
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    return []


def fetchDistinctDate(conn) -> list[datetime.date]:
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    # fetch distinct date from timetable
    return []


def fetchStdSub(conn, date: datetime.date) -> tuple[int, str]:
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    # returns the list of (std,sub) for a given date RETURN IN THIS ORDER ONLY
    std = 1
    sub = "eng"
    ...
    return std, sub


if __name__ == "__main__":
    import mysql.connector as mys
    import sqlite3
    conn = sqlite3.connect(".test.db")

    createSchema(conn)
