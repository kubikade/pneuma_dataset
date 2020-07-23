from math import sin, cos, sqrt, atan2, radians


def get_distance(datas_list, x):
    # approximate radius of earth in km
    R = 6378.0
    index = x - 1 if x - 1 > -1 else 0
    lat1 = radians(float(datas_list[index].lat))
    lon1 = radians(float(datas_list[index].lon))
    lat2 = radians(float(datas_list[x].lat))
    lon2 = radians(float(datas_list[x].lon))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000
    return distance


# x == lat, y == lon
def is_in_BBox(x, y, Bxmin, Bxmax, Bymin, Bymax):
    if Bxmin <= float(x) <= Bxmax:
        if Bymin <= float(y) <= Bymax:
            return True
        else:
            return False
    else:
        return False


def depart_from_BBox(vehicles, Bxmin, Bxmax, Bymin, Bymax):
    departing = []
    for vehicle in vehicles:
        if is_in_BBox(vehicle.datas_list[0].lat, vehicle.datas_list[0].lon, Bxmin, Bxmax, Bymin, Bymax):
            departing.append(vehicle)
    return departing


def pass_through_BBox(vehicles, Bxmin, Bxmax, Bymin, Bymax):
    passing = []
    for vehicle in vehicles:
        for i in range(len(vehicle.datas_list)):
            if is_in_BBox(vehicle.datas_list[i].lat, vehicle.datas_list[i].lon, Bxmin, Bxmax, Bymin, Bymax):
                passing.append(vehicle)
                break
    return passing
