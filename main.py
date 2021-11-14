import csv
from Building import Building
from Calls import Calls

building = Building("B1.json")
calls = []

with open("Calls_a.csv", 'r') as file:
    csvReader = csv.reader(file)
    for call in csvReader:
        currCall = Calls(call)
        calls.append(currCall)
    file.close()

building.calls = calls

with open("Ex1_Calls_case_2_a.csv", 'w') as file:
    csvWriter = csv.writer(file)
    for call in building.calls:
        row = building.output(call)
        csvWriter.writerow(row)
    file.close()
