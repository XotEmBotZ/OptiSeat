import datetime


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