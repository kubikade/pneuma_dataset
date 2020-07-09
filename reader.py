import csv
import Vehicle

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
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, i, row), get_VehData(filepath, i, row, granuality))
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
    vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, rowIndex, line), get_VehData(filepath, rowIndex, line, granuality))
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
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(filepath, i, row), get_VehData(filepath, i, row, granuality))
            vehicles.append(vehicle)
        return vehicles


# returns list of first 4 parameters for Vehicle object
def get_Vehicle_info(filepath, rowIndex, line):
    ret = []
    for i in range(4):
        ret.append(line[i])
    return ret

# returns fifth parameter for Vehicle object - list of VehData
def get_VehData(filepath, rowIndex, line, granuality=1):
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
        ret.append(Vehicle.VehData(*data))
        data = []
        i += 6 * (granuality - 1)
    return ret


path = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
vehicles_list = load_rows_in_interval(path, 0, 2, 1)
for veh in vehicles_list:
    print(veh)
