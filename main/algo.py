import datetime
import pickle
from pprint import pprint
import sqlite3

from sql import func as sql_func
from utils.types import ResultRoomSet, ResultStudentSet, RoomExtendedType, RoomType, StudentType
from utils.utils import checkStdSubExceedsNumBench , getDistinctStdSubSec


def allocateSeat(conn)->dict[str,dict[str,RoomExtendedType]]:
    rooms: list[RoomType]=sql_func.fetchRooms(conn)
    distinctDate: list[datetime.date]=sql_func.fetchDistinctDate(conn)
    res={}
    for date in distinctDate:
        stdSubPair: list[tuple[int, str]]=sql_func.fetchStdSub(conn,date)
        studLst: list[StudentType]=[]
        for pair in stdSubPair:
            studLst.extend(sql_func.fetchStud(conn,*pair))
        dateToomDict:dict[str,RoomExtendedType]={}
        addedStd=True
        allocationNo=1
        while len(studLst)>0:
            if not addedStd:
                raise AssertionError("Cannot allocate seat to all students (insufficent rooms)")
            addedStd=False
            for room in rooms:
                roomName: str=room["name"]
                if roomName not in dateToomDict:
                    dateToomDict[roomName]={**room,"studRaw":[]}
                
                if allocationNo<=dateToomDict[roomName]["benchStud"]:
                    dateToomDict[roomName]["studRaw"].extend(studLst[:min(len(studLst),dateToomDict[roomName]["numBench"])])
                    studLst=studLst[min(len(studLst),dateToomDict[roomName]["numBench"]):]
                    addedStd=True
            allocationNo+=1
        checkStdSubExceedsNumBench(list(dateToomDict.values()))
        res[date.strftime("%Y-%m-%d")]=dateToomDict
    return res

def postProcessRes(res:dict[str,dict[str,RoomExtendedType]]):
    resultSet:dict[str,list[ResultRoomSet]]={}
    for date,data in res.items():
        roomLst:list[ResultRoomSet]=[]
        for roomName,roomData in data.items():
            studRaw=roomData["studRaw"]
            resultStudentSetLst:list[ResultStudentSet]=[]
            for std,sub,sec in getDistinctStdSubSec(roomData):
                rollNo=[]
                for stud in studRaw:
                    if stud["std"]==std and stud["sub"]==sub and stud["sec"]==sec:
                        rollNo.append(stud["rollNo"])
                rollNo.sort()
                isSeq=all([(rollNo[index]-rollNo[index-1])==1 for index in range(1,len(rollNo)) ])
                resultStudentSet:ResultStudentSet={
                    "std":std,
                    "sub":sub,
                    "sec":sec,
                    "isSeq":isSeq,
                    "rollStart":None,
                    "rollEnd":None,
                    "rollArr":None,
                }
                if isSeq:
                    resultStudentSet["rollStart"]=rollNo[0]
                    resultStudentSet["rollEnd"]=rollNo[-1]
                else:
                    resultStudentSet["rollArr"]=rollNo
                resultStudentSetLst.append(resultStudentSet)
            resultRoomSet:ResultRoomSet={
                "name":roomName,
                "numBench":roomData["numBench"],
                "benchStud":roomData["benchStud"],
                "stud":resultStudentSetLst
            }
            roomLst.append(resultRoomSet)
        resultSet[date]=roomLst
    return resultSet
                        


if __name__=="__main__":
    conn=sqlite3.connect("test.sqlite3")
    pickle.dump(postProcessRes(allocateSeat(conn)),open("data.bin","wb"))
    
