import datetime
from typing import TypedDict

#TODO do subject type hint

class studentType(TypedDict):
    std:int
    sub:str
    rollNo:int

class RoomType(TypedDict):
    name:str
    numBench:int
    benchStud:int

class RoomExtendedType(RoomType):
    studRaw:list[studentType]

class RawStudentType(TypedDict):
    std:int
    sec:str
    sub:str
    isSeq:bool
    rollStart:int
    rollEnd:int
    rollArr:tuple[int,...]

class Timetable(TypedDict):
    date:datetime.date
    std:int
    sub:str