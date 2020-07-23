import utils
import reader
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.collections import LineCollection


def get_distance_list(vehicle):
    distanceList = []
    for i in range(len(vehicle.lat_list)):
        j = 0
        dist = 0.0
        while j <= i:
            dist += utils.get_distance(vehicle, j)
            j += 1
        distanceList.append(dist)
    return distanceList


"""def get_lists_of_all_vehicles(vehicles):
    lists = []
    for vehicle in vehicles:
        temp = get_distance_list(vehicle)
        lists.append(temp)
    return lists"""


def get_segments(time_list, distance_list):
    points = np.array([time_list, distance_list]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
granularity = 25
vehicles = []
numbers = " "
BBox = [37.98948, 37.99054, 23.73059, 23.73113]

BBoxleft = [37.99130, 37.99163, 23.73236, 23.73326]
BBoxright = [37.99083, 37.99102, 23.73559, 23.73694]
BBoxdown = [37.99134, 37.99157, 23.72996, 23.73061]
#2478 max index

#vehicles = reader.load_rows_in_interval(filepath, 150, 1860, granularity)
#dep = utils.depart_from_BBox(vehicles, *BBox)
vehicles = reader.load_rows_in_interval(filepath, 370, 400, granularity)
ll = utils.pass_through_BBox(vehicles, *BBoxleft)
rr = utils.pass_through_BBox(ll, *BBoxright)
dep = utils.pass_through_BBox(rr, *BBoxdown)

fig, ax = plt.subplots()
#alllists = get_lists_of_all_vehicles(dep)

mindist = min(get_distance_list(dep[0]))
maxdist = max(get_distance_list(dep[0]))
mintime = min(dep[0].time_list)
maxtime = max(dep[0].time_list)
minspeed = min(dep[0].speed_list)
maxspeed = max(dep[0].speed_list)

for i in range(len(dep)):
    print(dep[i])
    distance_list = get_distance_list(dep[i])
    minspeed = min(dep[i].speed_list) if min(dep[i].speed_list) < minspeed else minspeed
    maxspeed = max(dep[i].speed_list) if max(dep[i].speed_list) > maxspeed else maxspeed
    mindist = min(distance_list) if min(distance_list) < mindist else mindist
    maxdist = max(distance_list) if max(distance_list) > maxdist else maxdist
    mintime = min(dep[i].time_list) if min(dep[i].time_list) < mintime else mintime
    maxtime = max(dep[i].time_list) if max(dep[i].time_list) > maxtime else maxtime

norm = plt.Normalize(minspeed, maxspeed)
cmap = 'coolwarm'
lines = []

for i in range(len(dep)):
    seg = get_segments(dep[i].time_list, get_distance_list(dep[i]))
    lc = LineCollection(seg, cmap=cmap, norm=norm)
    lc.set_array(np.array(dep[i].speed_list))
    lc.set_linewidth(2)
    lc.set_label(dep[i].track_id + " " + dep[i].type)
    line = ax.add_collection(lc)

plt.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap), label="velocity [km/h]")
#plt.title("car no." + str(numbers))
plt.ylabel("distance [m]")
plt.xlabel("time [s]")
plt.grid()
plt.legend(loc="upper left")
ax.set_xlim(mintime, maxtime)
ax.set_ylim(mindist, maxdist)
plt.show()

