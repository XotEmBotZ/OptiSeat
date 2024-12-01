import datetime
from utils.types import RoomType, studentType


def createSchema(conn)->None:
    ...

def checkSchema(conn)->None:
    ...

#DO THE CHECKING IN THE FUNCTION ALSO
#like (for ef in std) as per the database schema -> assert len(sec)=1 , "Length of sec is not 1"

def insertRooms(conn,name:str,noBench:int,benchStd:int=2)-> int :
    #returns the generated ID
    return 0

def insertTeachers(conn,name:str,)-> int :
    #returns the generated ID
    return 0

def insertStudents(conn,std:int,sec:str,sub:str,isSeq:bool,rollStart:int=0,rollEnd:int=0,rollArr:list[int]|None=None)-> int :
    #returns the generated ID
    return 0

def insertTimetable(conn,date:datetime.date,std:int,sub:str)->int:
    #returns the generated ID
    return 0

def fetchRooms(conn)->list[RoomType]:
    #roomDict={name,no_bench,bench_std}
    ...

def fetchStud(conn,std:int,sub:str)->list[studentType]:
    #fetch students with given std and str
    #order by std,sub
    #return tuple as ([std,sub,rollNo],[std,sub,rollNo],[std,sub,rollNo])
    ...

def fetchDistinctDate(conn)->list[datetime.date]:
    #fetch distinct date from timetable
    ...

def fetchStdSub(conn,date:datetime.date)->tuple[int,str]:
    #returns the list of (std,sub) for a given date RETURN IN THIS ORDER ONLY
    std=1
    sub="eng"
    ...
    return std,sub