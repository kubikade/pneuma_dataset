from math import sin, cos, sqrt, atan2, radians


def get_distance(vehicle, x):
    # approximate radius of earth in km
    R = 6378.0
    index = x - 1 if x - 1 > -1 else 0
    lat1 = radians(float(vehicle.lat_list[index]))
    lon1 = radians(float(vehicle.lon_list[index]))
    lat2 = radians(float(vehicle.lat_list[x]))
    lon2 = radians(float(vehicle.lon_list[x]))
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
        if is_in_BBox(vehicle.lat_list[0], vehicle.lon_list[0], Bxmin, Bxmax, Bymin, Bymax):
            departing.append(vehicle)
    return departing


def pass_through_BBox(vehicles, Bxmin, Bxmax, Bymin, Bymax):
    passing = []
    for vehicle in vehicles:
        for i in range(len(vehicle.lat_list)):
            if is_in_BBox(vehicle.lat_list[i], vehicle.lon_list[i], Bxmin, Bxmax, Bymin, Bymax):
                passing.append(vehicle)
                break
    return passing


def pass_through_Polygon(trajectories, Polygon):
    intersecting = trajectories.get_intersecting(Polygon)
    return intersecting

def pass_through_Polygons(trajectories, Polygons):
    temp = trajectories
    for Polygon in Polygons:
        intersecting = temp.get_intersecting(Polygon)
        temp = intersecting
    return intersecting