from utils.types import RawStudentType, RoomExtendedType, RoomType, Timetable
from sql import func
import xlsxwriter
import io

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

def getXlsxFile(data,filename):
    def writeClass(room,worksheet,row,border):
        worksheet.merge_range(row,0,row+1+len(room["stud"]),0,room["name"],border)
        worksheet.write(row,1,"No. Bench:",border)
        worksheet.write(row,2,room["numBench"],border)
        worksheet.write(row,3,"Student/Bench:",border)
        worksheet.write(row,4,room["benchStud"],border)
        row+=1
        worksheet.write(row,1,"Class-Sec",border)
        worksheet.write(row,2,"Subject",border)
        worksheet.merge_range(row,3,row,4,"Roll",border)
        row+=1
        for stdSec in room["stud"]:
            worksheet.write(row,1,str(stdSec["std"])+"-"+stdSec["sec"],border)
            worksheet.write(row,2,stdSec["sub"],border)
            if stdSec["isSeq"]:
                worksheet.write(row,3,stdSec["rollStart"],border)
                worksheet.write(row,4,stdSec["rollEnd"],border)
            else:
                worksheet.merge_range(row,3,row,4,str(stdSec["rollArr"]).replace("[","").replace("]",""))
            row+=1
        return row
    opt=io.BytesIO()
    workbook=xlsxwriter.Workbook(opt,{"in_memory":True})
    border=workbook.add_format({'border':1, 'border_color':'black'})
    for date,roomLst in data.items():
        worksheet=workbook.add_worksheet(date)
        row=0
        for room in roomLst:
            row=writeClass(room,worksheet,row,border)
            row+=1
        worksheet.autofit()
    workbook.close()
    return opt.getvalue()