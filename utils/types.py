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