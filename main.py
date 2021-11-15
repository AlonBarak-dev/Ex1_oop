import csv
from Building import Building
from Calls import Calls


def json_Build(pathJson):
    return Building(pathJson)

def csv_Build(pathCsv):
    calls = []
    with open(pathCsv, 'r') as file:
        csvReader = csv.reader(file)
        for call in csvReader:
            currCall = Calls(call)
            calls.append(currCall)
        file.close()
    building.calls = calls

def csv_Writer(pathCsvW):
    with open(pathCsvW, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        for call in building.calls:
            row = building.output(call)
            if len(row) != 0:
                csvWriter.writerow(row)
        file.close()


if __name__ == '__main__':
    pathJson = "files/Ex1_Buildings/B5.json"
    building = json_Build(pathJson)
    pathCsv = "files/Ex1_Calls/Calls_b.csv"
    csv_Build(pathCsv)
    pathCsvOut = "files/Ex1_Output/Ex1_Calls_case_5_b.csv"
    csv_Writer(pathCsvOut)

