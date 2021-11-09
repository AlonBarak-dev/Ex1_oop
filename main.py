import json
import csv
from Building import Building
from Calls import Calls
from Elevator import Elevator
"""
Reading the json file and creating new objects of building and elevator from
it.
"""
f = open('B1.json', )
data = json.load(f)
listOfElevators = []
for v in data['_elevators']:
    elevator = Elevator(id = v['_id'], speed = v['_speed'], minFloor = v['_minFloor'], maxFloor = v['_maxFloor'], closeTime = v['_closeTime'],
                        openTime = v['_openTime'],startTime = v['_startTime'], stopTime = v['_stopTime'],currentDirection = False,
                        listOfCalls = [1,2,3], currentFloor = 0)
    listOfElevators.append(elevator)

numberOfElevator = len(listOfElevators)
building = Building(minFloor = data["_minFloor"], maxFloor = data['_maxFloor'], elevators = listOfElevators, numberOfElevators = numberOfElevator)

"""
End of creating building
"""
#################
"""
Reading from the csv filer and creating objects of calls
"""

calls = []
with open("Calls_a.csv", 'r') as file:
    csvReader = csv.reader(file)
    for call in csvReader:
        currentCall = Calls(text= call[0], time= call[1], source= call[2], destination= call[3], state=call[4], allocateTo=0,currentDirc= False, timeReceived= 0.0)
        calls.append(currentCall)

"""
END of creating list of calls from the file
"""









