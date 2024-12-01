import datetime

from utils.types import RoomType, studentType
from utils.utils import cvtLstIntToSql


def createSchema(conn) -> None:
    cursor = conn.cursor()
    query = open(r"sql\schema.sql").read()
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
    assert len(name) <= 3, "Length of sec name is more than 3"
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


def insertTimetable(conn,date:datetime.date,std:int,sub:str)->int:
    #returns the generated ID
    return 0

def fetchRooms(conn)->dict[str,str|int|list|dict]:
    #roomDict={name,no_bench,bench_std,stdRaw:[],finalOpt:{}}
    ...

def fetchStd(conn)->list[tuple[str|int]]:
    #return tuple as ([std,sub,rollNo],[std,sub,rollNo],[std,sub,rollNo])
    ...

def fetchDistinctDate(conn) -> list[datetime.date]:
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    # fetch distinct date from timetable
    return []


def fetchStdSub(conn,date:datetime.date)->list[list[str|int]]:
    #returns the list of (std,sub) for a given date RETURN IN THIS ORDER ONLY
    ...