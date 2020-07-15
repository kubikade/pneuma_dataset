import utils
import reader
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
granularity = 5
carnumber = 25
carnumber2 = 26
veh1 = reader.load_one_row(filepath, carnumber+1, granularity)
print(veh1)

timeList = []
distanceList = []
speedList = []

for i in range(len(veh1.datas_list)):
    time = veh1.datas_list[i].time
    #timeList.append(time)
    sep = "."
    rest = time.split(sep, 1)[0]
    rest = (float(rest) / 1000)
    timeList.append(rest)
    j = 0
    dist = 0.0
    while j <= i:
        dist += utils.get_distance(veh1.datas_list, j)
        j += 1
    distanceList.append(dist)
    speed = veh1.datas_list[i].speed
    speedList.append(float(speed))

veh2 = reader.load_one_row(filepath, carnumber2+1, granularity)
print(veh2)

timeList2 = []
distanceList2 = []
speedList2 = []

for i in range(len(veh2.datas_list)):
    time = veh2.datas_list[i].time
    #timeList.append(time)
    sep = "."
    rest = time.split(sep, 1)[0]
    rest = (float(rest) / 1000)
    timeList2.append(rest)
    j = 0
    dist = 0.0
    while j <= i:
        dist += utils.get_distance(veh2.datas_list, j)
        j += 1
    distanceList2.append(dist)
    speed = veh2.datas_list[i].speed
    speedList2.append(float(speed))

x = np.array(timeList)
y = np.array(distanceList)
#dydx = np.diff(y) / np.diff(x) * 3.6
dydx = np.array(speedList)
points = np.array([timeList, distanceList]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

x2 = np.array(timeList2)
y2 = np.array(distanceList2)
#dydx = np.diff(y) / np.diff(x) * 3.6
dydx2 = np.array(speedList2)
points2 = np.array([timeList2, distanceList2]).T.reshape(-1, 1, 2)
segments2 = np.concatenate([points2[:-1], points2[1:]], axis=1)

fig = plt.subplot()
norm = plt.Normalize(min(dydx), max(dydx))
lc = LineCollection(segments, cmap='coolwarm', norm=norm)
# RdYlGn
lc.set_array(dydx)
lc.set_linewidth(2)
line = fig.add_collection(lc)
plt.colorbar(line, label="velocity [km/h]")

lc2 = LineCollection(segments2, cmap='coolwarm', norm=norm)
lc2.set_array(dydx2)
lc2.set_linewidth(2)
line2 = fig.add_collection(lc2)

plt.title("car no." + str(carnumber))
plt.ylabel("distance [m]")
plt.xlabel("time [s]")
plt.grid()
fig.set_xlim(0, max(x))
fig.set_ylim(min(y), max(y))
plt.show()



