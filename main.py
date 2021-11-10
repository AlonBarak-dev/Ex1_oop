import json
import csv
from Building import Building
from Calls import Calls
from Elevator import Elevator


building = Building("B1.json")
calls = []
with open("Calls_a.csv", 'r') as file:
    csvReader = csv.reader(file)
    for call in csvReader:
        currCall = Calls(call)
        calls.append(currCall)










