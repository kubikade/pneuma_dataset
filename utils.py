from math import sin, cos, sqrt, atan2, radians
import movingpandas as mpd
from shapely.geometry import Polygon, Point


def get_distance(vehicle, x):
    # approximate radius of earth in km
    r = 6378.0
    index = x - 1 if x - 1 > -1 else 0
    lat1 = radians(float(vehicle.lat_list[index]))
    lon1 = radians(float(vehicle.lon_list[index]))
    lat2 = radians(float(vehicle.lat_list[x]))
    lon2 = radians(float(vehicle.lon_list[x]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c * 1000
    return distance


# x == lat, y == lon
def is_in_bbox(x, y, bxmin, bxmax, bymin, bymax):
    if bxmin <= float(x) <= bxmax:
        if bymin <= float(y) <= bymax:
            return True
        else:
            return False
    else:
        return False


def depart_from_bbox(vehicles, bxmin, bxmax, bymin, bymax):
    departing = []
    for vehicle in vehicles:
        if is_in_bbox(vehicle.lat_list[0], vehicle.lon_list[0], bxmin, bxmax, bymin, bymax):
            departing.append(vehicle)
    return departing


def pass_through_bbox(vehicles, bxmin, bxmax, bymin, bymax):
    passing = []
    for vehicle in vehicles:
        for i in range(len(vehicle.lat_list)):
            if is_in_bbox(vehicle.lat_list[i], vehicle.lon_list[i], bxmin, bxmax, bymin, bymax):
                passing.append(vehicle)
                break
    return passing


def veh_depart_from_polygon(vehicles, polygon):
    departing = []
    for vehicle in vehicles:
        if Point(vehicle.lon_list[0], vehicle.lat_list[0]).within(polygon):
            departing.append(vehicle)
    return departing


def veh_pass_through_polygon(vehicles, polygon):
    passing = []
    for vehicle in vehicles:
        for i in range(len(vehicle.lat_list)):
            if Point(vehicle.lon_list[i], vehicle.lat_list[i]).within(polygon):
                passing.append(vehicle)
                break
    return passing


def veh_pass_through_polygons(vehicles, polygons):
    passing = vehicles
    for polygon in polygons:
        temp = passing
        passing = []
        for vehicle in temp:
            for i in range(len(vehicle.lat_list)):
                if Point(vehicle.lon_list[i], vehicle.lat_list[i]).within(polygon):
                    passing.append(vehicle)
                    break
    return passing


def traj_through_polygon(trajectories, polygon):
    intersecting = trajectories.get_intersecting(polygon)
    return intersecting


def traj_through_polygons(trajectories, polygons):
    temp = trajectories
    for polygon in polygons:
        intersecting = temp.get_intersecting(polygon)
        temp = intersecting
    return intersecting


def gdf_num_of_cars_through_polygon(gdf, polygon):
    trajectories = mpd.TrajectoryCollection(gdf, 'track_id')
    intersecting = trajectories.get_intersecting(polygon)
    return len(intersecting)


def gdf_num_of_cars_through_polygons(gdf, polygons):
    temp = mpd.TrajectoryCollection(gdf, 'track_id')
    for polygon in polygons:
        intersecting = temp.get_intersecting(polygon)
        temp = intersecting
    return len(intersecting)


def gdf_num_and_traj_list_of_cars_through_polygon(gdf, polygon):
    trajectories = mpd.TrajectoryCollection(gdf, 'track_id')
    intersecting = trajectories.get_intersecting(polygon)
    return len(intersecting), intersecting


def gdf_num_and_traj_list_cars_through_polygons(gdf, polygons):
    temp = mpd.TrajectoryCollection(gdf, 'track_id')
    for polygon in polygons:
        intersecting = temp.get_intersecting(polygon)
        temp = intersecting
    return len(intersecting), intersecting
