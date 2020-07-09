import csv
import Vehicle

"""
USELESS
def load_multiple_rows(filepath, number, granuality=1):
    vehicles = []
    for x in range(number):
        vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, x), get_Veh_data(filepath, x, granuality))
        vehicles.append(vehicle)
    return vehicles
    

USELESS
def load_line(filepath, rowIndex):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        line = []
        for i in range(rowIndex+1):
            temporary = next(reader)
        for val in temporary:
            val = val.replace(" ", "")
            line.append(val)
        return line
        

USELESS
def get_Veh_data_granuality(filepath, rowIndex, granuality):
    line = load_line(filepath, rowIndex)
    ret = []
    data = []
    i = 4
    counter = 0
    while i < len(line)-1:
        while counter < 6:
            data.append(line[i])
            i += 1
            counter += 1
        counter = 0
        ret.append(Vehicle.Veh_data(*data))
        data = []
        i += 6*(granuality-1)
    return ret
"""


def get_number_of_rows(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        row_count = sum(1 for row in reader)
    return row_count


# load first NROWS lines
def load_multiple_rows(filepath, nrows, granuality):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        vehicles = []
        for i in range(nrows):
            row = []
            temporary = next(reader)
            for val in temporary:
                val = val.replace(" ", "")
                row.append(val)
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, i, row), get_Veh_data(filepath, i, row, granuality))
            vehicles.append(vehicle)
        return vehicles


# load one row on exact index - rowIndex
def load_one_row(filepath, rowIndex, granuality = 1):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        line = []
        for i in range(rowIndex):
            temporary = next(reader)
        for val in temporary:
            val = val.replace(" ", "")
            line.append(val)
    vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, rowIndex, line), get_Veh_data(filepath, rowIndex, line, granuality))
    return vehicle


def load_rows_in_interval(filepath, fromIndex, toIndex, granuality=1):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for i in range(fromIndex):
            temporary = next(reader)
        vehicles = []
        for i in range(toIndex - fromIndex + 1):
            row = []
            temporary = next(reader)
            for val in temporary:
                val = val.replace(" ", "")
                row.append(val)
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, i, row), get_Veh_data(filepath, i, row, granuality))
            vehicles.append(vehicle)
        return vehicles


# returns list of first 4 parameters for Vehicle object
def get_Vehicle_info(filepath, rowIndex, line):
    ret = []
    for i in range(4):
        ret.append(line[i])
    return ret

# returns fifth parameter for Vehicle object - list of Veh_data
def get_Veh_data(filepath, rowIndex, line, granuality=1):
    ret = []
    data = []
    i = 4
    counter = 0
    while i < len(line)-1:
        while counter < 6:
            data.append(line[i])
            i += 1
            counter += 1
        counter = 0
        ret.append(Vehicle.Veh_data(*data))
        data = []
        i += 6 * (granuality - 1)
    return ret


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"

vehicles = load_rows_in_interval(filepath, 1345, 1345, 1)
for veh in vehicles:
    print(str(veh))
    print(veh)
    print(repr(veh))
"""
minLat = vehicles[1].findMinLat()
maxLat = vehicles[1].findMaxLat()
minLon = vehicles[1].findMinLon()
maxLon = vehicles[1].findMaxLon()
print("init " + minLat, maxLat, minLon, maxLon)

for x in range(len(vehicles)-1):
    minLat = vehicles[x+1].findMinLat() if vehicles[x+1].findMinLat() < minLat else minLat
    maxLat = vehicles[x+1].findMaxLat() if vehicles[x+1].findMaxLat() > maxLat else maxLat
    minLon = vehicles[x+1].findMinLon() if vehicles[x+1].findMinLon() < minLon else minLon
    maxLon = vehicles[x+1].findMaxLon() if vehicles[x+1].findMaxLon() > maxLon else maxLon

print("minMAX lat, lon: " + minLat, maxLat, minLon, maxLon)
"""








