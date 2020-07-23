import utils
import reader
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.collections import LineCollection


def loadLists(vehicle):
    timeList = []
    distanceList = []
    speedList = []
    for i in range(len(vehicle.datas_list)):
        time = vehicle.datas_list[i].time
        sep = "."
        rest = time.split(sep, 1)[0]
        rest = (float(rest) / 1000)
        timeList.append(rest)
        j = 0
        dist = 0.0
        while j <= i:
            dist += utils.get_distance(vehicle.datas_list, j)
            j += 1
        distanceList.append(dist)
        speed = vehicle.datas_list[i].speed
        speedList.append(float(speed))
    return timeList, distanceList, speedList


def get_lists_of_all_vehicles(vehicles):
    lists = []
    for vehicle in vehicles:
        temp = loadLists(vehicle)
        lists.append(temp)
    return lists


def get_segments(timeList, distanceList, speedList):
    points = np.array([timeList, distanceList]).T.reshape(-1, 1, 2)
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
vehicles = reader.load_rows_in_interval(filepath, 380, 400, granularity)
ll = utils.pass_through_BBox(vehicles, *BBoxleft)
rr = utils.pass_through_BBox(ll, *BBoxright)
dep = utils.pass_through_BBox(rr, *BBoxdown)

fig, ax = plt.subplots()
alllists = get_lists_of_all_vehicles(dep)

mindist = min(alllists[0][1])
maxdist = max(alllists[0][1])
mintime = min(alllists[0][0])
maxtime = max(alllists[0][0])
minspeed = min(alllists[0][2])
maxspeed = max(alllists[0][2])

for i in range(len(dep)):
    print(vehicles[i])
    minspeed = min(alllists[i][2]) if min(alllists[i][2]) < minspeed else minspeed
    maxspeed = max(alllists[i][2]) if max(alllists[i][2]) > maxspeed else maxspeed
    mindist = min(alllists[i][1]) if min(alllists[i][1]) < mindist else mindist
    maxdist = max(alllists[i][1]) if max(alllists[i][1]) > maxdist else maxdist
    mintime = min(alllists[i][0]) if min(alllists[i][0]) < mintime else mintime
    maxtime = max(alllists[i][0]) if max(alllists[i][0]) > maxtime else maxtime

norm = plt.Normalize(minspeed, maxspeed)
cmap = 'coolwarm'
lines = []

for i in range(len(dep)):
    seg = get_segments(*alllists[i])
    lc = LineCollection(seg, cmap=cmap, norm=norm)
    lc.set_array(np.array(alllists[i][2]))
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

