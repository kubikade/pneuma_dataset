import utils
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.collections import LineCollection


def get_distance_list(vehicle):
    distance_list = []
    for i in range(len(vehicle.lat_list)):
        j = 0
        dist = 0.0
        while j <= i:
            dist += utils.get_distance(vehicle, j)
            j += 1
        distance_list.append(dist)
    return distance_list


def get_segments(time_list, distance_list):
    points = np.array([time_list, distance_list]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments


def find_minimum_maximum(vehicles):
    min_dist = min(get_distance_list(vehicles[0]))
    max_dist = max(get_distance_list(vehicles[0]))
    min_time = min(vehicles[0].time_list)
    max_time = max(vehicles[0].time_list)
    min_speed = min(vehicles[0].speed_list)
    max_speed = max(vehicles[0].speed_list)
    for vehicle in vehicles:
        distance_list = get_distance_list(vehicle)
        min_speed = min(vehicle.speed_list) if min(vehicle.speed_list) < min_speed else min_speed
        max_speed = max(vehicle.speed_list) if max(vehicle.speed_list) > max_speed else max_speed
        min_dist = min(distance_list) if min(distance_list) < min_dist else min_dist
        max_dist = max(distance_list) if max(distance_list) > max_dist else max_dist
        min_time = min(vehicle.time_list) if min(vehicle.time_list) < min_time else min_time
        max_time = max(vehicle.time_list) if max(vehicle.time_list) > max_time else max_time
    return min_dist, max_dist, min_time, max_time, min_speed, max_speed


def to_plot(vehicles):
    min_dist, max_dist, min_time, max_time, min_speed, max_speed = find_minimum_maximum(vehicles)
    fig, ax = plt.subplots()
    norm = plt.Normalize(min_speed, max_speed)
    colormap = 'coolwarm'
    for vehicle in vehicles:
        seg = get_segments(vehicle.time_list, get_distance_list(vehicle))
        lc = LineCollection(seg, cmap=colormap, norm=norm)
        lc.set_array(np.array(vehicle.speed_list))
        lc.set_linewidth(2)
        lc.set_label(vehicle.track_id + " " + vehicle.type)
        ax.add_collection(lc)
    plt.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=colormap), label="velocity [km/h]")
    plt.ylabel("distance [m]")
    plt.xlabel("time [s]")
    plt.grid()
    plt.legend(loc="upper left")
    ax.set_xlim(min_time, max_time)
    ax.set_ylim(min_dist, max_dist)
    plt.show()
