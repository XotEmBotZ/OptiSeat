from sql import func as head
import datetime

def insertRooms(conn) -> None:
    name: str = input("Enter Room Name:")
    numBenches = int(input("Enter number of benches:"))
    benchStud: str|int = input("Enter number of students per bench (default:2):")
    if benchStud == "":
        benchStud = 2
    else:
        benchStud = int(benchStud)
    head.insertRooms(conn,name,numBenches,benchStud)


def insertStudents(conn)->None:
	std:int = int(input("Enter Standard:"))
	sec:str = input("Enter Section:")
	sub:str = input("Enter Suject:")
	isSeq:str|bool = str(input("Does every student taking the subject have their roll no. sequential(Y/N):"))
	if isSeq.lower() == "y":
		isSeq = True
		rollStart:int = int(input("Enter Starting roll no.:"))
		rollEnd:int = int(input("Enter Ending roll no.:"))
		head.insertStudents(conn,std,sec,sub,isSeq,rollStart,rollEnd)

	else:
		isSeq = False
		rollArr:list[int]=[]
		n:int = int(input("How many students have the taking subject:"))
		for i in range(n):
			dat = int(input(f"Enter roll number of the student no.{i+1}"))
			rollArr.append(dat)
		head.insertStudents(conn,std,sec,sub,isSeq,rollArr=rollArr)


def insertTeachers(conn)->None:
	name:str = input("Enter teacher name:")
	head.insertTeachers(conn,name)


def insertTimetable(conn) ->None:
	a:int = int(input("Enter date (0-31):"))
	b:int = int(input("Enter month (0-12):"))
	c:int = int(input("Enter year (20XX):"))
	date:datetime.date = datetime.date(a,b,c)
	std:int = int(input("Enter Grade:"))
	sub:str = input("Enter Subject:")
	head.insertTimetable(conn,date,std,sub)