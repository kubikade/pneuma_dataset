import csv
import Vehicle


def get_number_of_rows(filepath):
    """get_number_of_rows.

    Args:
        filepath: path to a csv file.

    Returns:
        row_count: number of rows in csv file
    """
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        row_count = sum(1 for row in reader)
    return row_count


# load first NROWS lines
def load_multiple_rows(filepath, nrows, granularity=25):
    """load_multiple_rows.

    Args:
        filepath: path to a csv file.
        nrows: number of rows to be loaded
        granularity: granularity of data, granularity 20 - each 20th data input will be loaded

    Returns:
       vehicles: list of Vehicle type objects.
    """
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        vehicles = []
        next(reader)
        for i in range(nrows):
            row = []
            temporary = next(reader)
            for val in temporary:
                val = val.replace(" ", "")
                row.append(val)
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(row), *get_VehData(row, granularity))
            vehicles.append(vehicle)
        return vehicles


# load one row on exact index - rowIndex
def load_one_row(filepath, rowIndex, granularity=25):
    """load_one_row.

    Args:
        filepath: path to a csv file.
        rowIndex: index of row to be loaded
        granularity: granularity of data, granularity 20 - each 20th data input will be loaded

    Returns:
       vehicle: Vehicle type object.
    """
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        line = []
        for i in range(rowIndex):
            temporary = next(reader)
        for val in temporary:
            val = val.replace(" ", "")
            line.append(val)
    vehicle = Vehicle.Vehicle(*get_Vehicle_info(line), *get_VehData(line, granularity))
    return vehicle


def load_rows_in_interval(filepath, fromIndex, toIndex, granularity=25):
    """load_rows_in_interval.

    Args:
        filepath: path to a csv file.
        fromIndex: index of first row to be loaded
        toIndex: index of last row to be loaded
        granularity: granularity of data, granularity 20 - each 20th data input will be loaded

    Returns:
       vehicles: list of Vehicle type objects.
    """
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
            vehicle = Vehicle.Vehicle(*get_Vehicle_info(row), *get_VehData(row, granularity))
            vehicles.append(vehicle)
        return vehicles


# returns list of first 4 parameters for Vehicle object
def get_Vehicle_info(line):
    """get_Vehicle_info.

    Args:
        line: list of words representing one row in csv file

    Returns:
        ret: list of first four Vehicle object arguments
    """
    ret = []
    number_of_info = 4
    for i in range(number_of_info):
        ret.append(line[i])
    return ret


# returns lists of data for Vehicle objects
def get_VehData(line, granularity=25):
    """get_VehData.

    Args:
        line: list of words representing one row in csv file
        granularity: granularity of data, granularity 20 - each 20th data input will be loaded

    Returns:
        lat_list, lon_list, speed_list, tan_accel_list, lat_accel_list,
        time_list: lists with data inputs
    """
    lat_list = []
    lon_list = []
    speed_list = []
    tan_accel_list = []
    lat_accel_list = []
    time_list = []
    offset = i = 4
    number_of_data = 6
    while i < len(line)-1:
        lat_list.append(float(line[i]))
        lon_list.append(float(line[i+1]))
        speed_list.append(float(line[i+2]))
        tan_accel_list.append(float(line[i+3]))
        lat_accel_list.append(float(line[i+4]))
        time_list.append(float(line[i+5])/1000)
        i += (number_of_data * granularity)
    if len(lat_list) == len(lon_list) == len(speed_list) == len(tan_accel_list) == len(lat_accel_list) == len(time_list):
        return lat_list, lon_list, speed_list, tan_accel_list, lat_accel_list, time_list
    else:
        return None
