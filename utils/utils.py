from utils.types import RawStudentType, RoomExtendedType, RoomType, Timetable
from sql import func

def numStdSubStud(room:RoomExtendedType,std:int,sub:str)->int:
    count = 0
    for studRaw in room['studRaw']:
        if studRaw['std'] == std and studRaw['sub']== sub:
            count+=1
    return count

def getDistinctStdSub(room:RoomExtendedType) -> list[tuple[int, str]]:
    stdSubLst:list[tuple[int,str]]=[]
    for stud in room["studRaw"]:
        stdSub=(stud['std'],stud['sub'])
        if  stdSub not in stdSubLst:
            stdSubLst.append(stdSub)
    return stdSubLst

def getDistinctStdSubSec(room:RoomExtendedType) -> list[tuple[int, str,str]]:
    stdSubSecLst:list[tuple[int,str,str]]=[]
    for stud in room["studRaw"]:
        stdSubSec=(stud['std'],stud['sub'],stud["sec"])
        if  stdSubSec not in stdSubSecLst:
            stdSubSecLst.append(stdSubSec)
    return stdSubSecLst

def checkStdSubExceedsNumBench(roomList:list[RoomExtendedType]):
    for room in roomList:
        distinctStdSub: list[tuple[int, str]]= getDistinctStdSub(room)
        for stdSub in distinctStdSub:
            assert not numStdSubStud(room,*stdSub) > room['numBench'], "Number of students having same standard and subject is more than number of benches (insufficient rooms)"
            
def cvtLstIntToSql(integer_list):
    formatted_string = ', '.join(str(num) for num in integer_list)
    return f"({formatted_string})"


def insertManyRooms(conn,rooms:list[RoomType])->None:
    for room in rooms:
        func.insertRoom(conn,room["name"],room["numBench"],room["benchStud"])

def insertManyStuds(conn,studLst:list[RawStudentType])->None:
    for stud in studLst:
        if stud["isSeq"]:
            func.insertStudent(conn,stud["std"],stud["sec"],stud["sub"],stud["isSeq"],stud["rollStart"],stud["rollEnd"])
        else:
            func.insertStudent(conn,stud["std"],stud["sec"],stud["sub"],stud["isSeq"],rollArr=stud["rollArr"])

def insertManyTimetable(conn,ttList:list[Timetable])->None:
    for tt in ttList:
        func.insertTimetable(conn,tt["date"],tt["std"],tt["sub"])