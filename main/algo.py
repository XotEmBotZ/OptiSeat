import datetime

from sql import func as sql_func
from utils.types import RoomExtendedType, RoomType, studentType
from utils.utils import checkStdSubExceedsNumBench


def allocateSeat(conn)->dict[str,dict[str,RoomExtendedType]]:
    rooms: list[RoomType]=sql_func.fetchRooms(conn)
    distinctDate: list[datetime.date]=sql_func.fetchDistinctDate(conn)
    res={}
    for date in distinctDate:
        (std,sub)=sql_func.fetchStdSub(conn,date)
        stdLst: list[studentType]=sql_func.fetchStud(conn,std,sub)
        dateDict:dict[str,RoomExtendedType]={}
        addedStd=True
        allocationNo=1
        while len(stdLst)>0:
            if not addedStd:
                raise AssertionError("Cannot allocate seat to all students (insufficent rooms)")
            addedStd=False
            for room in rooms:
                roomName: str=room["name"]
                if room not in dateDict:
                    dateDict[roomName]={**room,"studRaw":[]}
                
                if allocationNo<=dateDict[roomName]["benchStud"]:
                    dateDict[roomName]["studRaw"].extend(stdLst[:min(len(stdLst),[dateDict[roomName]["numBench"]])])
                    stdLst=stdLst[min(len(stdLst),dateDict[roomName]["numBench"]):]
                    addedStd=True
            allocationNo+=1
        checkStdSubExceedsNumBench(list(dateDict.values()))
        res[date.strftime("%Y-%m-%d")]=dateDict
    return res


