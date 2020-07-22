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


def get_segments(timeList, distanceList, speedList):
    points = np.array([timeList, distanceList]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
granularity = 25
vehicles = []
numbers = " "
BBox = [37.98948, 37.99054, 23.73059, 23.73113]
#2478 max index

vehicles = reader.load_rows_in_interval(filepath, 1750, 1860, granularity)

fig, ax = plt.subplots()

#lists = loadLists(vehicles[0])

for vehicle in vehicles:
    if utils.is_in_BBox(vehicle.datas_list[0].lat, vehicle.datas_list[0].lon, *BBox):
        lists = loadLists(vehicle)
        mindist = min(lists[1])
        maxdist = max(lists[1])
        mintime = min(lists[0])
        maxtime = max(lists[0])
        minspeed = min(lists[2])
        maxspeed = max(lists[2])
        break

for vehicle in vehicles:
    if utils.is_in_BBox(vehicle.datas_list[0].lat, vehicle.datas_list[0].lon, *BBox):
        print(vehicle)
        #numbers += vehicle.track_id + ", "
        lists = loadLists(vehicle)
        minspeed = min(lists[2]) if min(lists[2]) < minspeed else minspeed
        maxspeed = max(lists[2]) if max(lists[2]) > maxspeed else maxspeed
        mindist = min(lists[1]) if min(lists[1]) < mindist else mindist
        maxdist = max(lists[1]) if max(lists[1]) > maxdist else maxdist
        mintime = min(lists[0]) if min(lists[0]) < mintime else mintime
        maxtime = max(lists[0]) if max(lists[0]) > maxtime else maxtime

norm = plt.Normalize(minspeed, maxspeed)
cmap = 'coolwarm'
lines = []


for vehicle in vehicles:
    if utils.is_in_BBox(vehicle.datas_list[0].lat, vehicle.datas_list[0].lon, *BBox):
        lists = loadLists(vehicle)
        seg = get_segments(*lists)
        lc = LineCollection(seg, cmap=cmap, norm=norm)
        lc.set_array(np.array(lists[2]))
        lc.set_linewidth(2)
        lc.set_label(vehicle.track_id + " " + vehicle.type)
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

