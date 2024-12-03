import datetime
from typing import TypedDict

#TODO do subject type hint

class StudentType(TypedDict):
    std:int
    sub:str
    sec:str
    rollNo:int

class RoomType(TypedDict):
    name:str
    numBench:int
    benchStud:int

class RoomExtendedType(RoomType):
    studRaw:list[StudentType]

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

class ResultStudentSet(TypedDict):
    std:int
    sub:str
    sec:str
    isSeq:bool
    rollStart:int|None
    rollEnd:int|None
    rollArr:tuple[int,...]|None

class ResultRoomSet(RoomType):
    name:str
    numBench:int
    benchStud:int
    stud:list[ResultStudentSet]