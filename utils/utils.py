from utils.types import RoomExtendedType


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

def checkStdSubExceedsNumBench(roomList:list[RoomExtendedType]):
    for room in roomList:
        distinctStdSub: list[tuple[int, str]]= getDistinctStdSub(room)
        for stdSub in distinctStdSub:
            assert numStdSubStud(room,*stdSub) > room['numBench'], "Number of students having same standard and subject is more than number of benches (insufficient rooms)"