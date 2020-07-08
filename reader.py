import csv
import Vehicle

def getNumberOfRows(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        row_count = sum(1 for row in reader)
    return row_count


def load_multiple_rows(filepath, number, granuality = 1):
    vehicles = []
    for x in range(number):
        vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, x), get_Veh_data_granuality(filepath, x, granuality))
        vehicles.append(vehicle)
    return vehicles


def load_one_row(filepath, index, granuality = 1):
    vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, index), get_Veh_data_granuality(filepath, index, granuality))
    return vehicle


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


def get_Vehicle_info(filepath, rowIndex):
    line = load_line(filepath, rowIndex)
    ret = []
    for i in range(4):
        s = line[i]
        s = s.replace(" ", "")
        ret.append(s)
    return ret


def get_Veh_data(filepath, rowIndex):
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
    return ret


def get_Veh_data_granuality(filepath, rowIndex, granuality):
    line = load_line(filepath, rowIndex)
    ret = []
    data = []
    i = 4
    offset = 4
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


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
""""
veh1 = load_one_row(filepath, 3)
print(veh1.toString())
print("min and max lat: " + veh1.findMinLat() + ", " + veh1.findMaxLat())
print("min and max lon: " + veh1.findMinLon() + ", " + veh1.findMaxLon())
print("len veh1 datasList: " + str(len(veh1.datas_list)))

print()

veh2 = load_one_row(filepath, 3, 3)
#print(veh2.toString())
print("min and max lat: " + veh2.findMinLat() + ", " + veh2.findMaxLat())
print("min and max lon: " + veh2.findMinLon() + ", " + veh2.findMaxLon())
print("len veh2 datasList: " + str(len(veh2.datas_list)))

print()
"""

vehicles = load_multiple_rows(filepath, 100)
car = load_one_row(filepath, 0)
print(car.toString())
print()


minLat = vehicles[1].findMinLat()
maxLat = vehicles[1].findMaxLat()
minLon = vehicles[1].findMinLon()
maxLon = vehicles[1].findMaxLon()

for x in range(len(vehicles)-1):
    minLat = vehicles[x+1].findMinLat() if vehicles[x+1].findMinLat() < minLat else minLat
    maxLat = vehicles[x+1].findMaxLat() if vehicles[x+1].findMaxLat() > maxLat else maxLat
    minLon = vehicles[x+1].findMinLon() if vehicles[x+1].findMinLon() < minLon else minLon
    maxLon = vehicles[x+1].findMaxLon() if vehicles[x+1].findMaxLon() > maxLon else maxLon
    if x == 0:
        print(minLat, maxLat, minLon, maxLon)
    #print(vehicles[x].toString())
print("minMAX lat, lon: " + minLat, maxLat, minLon, maxLon)







