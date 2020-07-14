import utils
import reader
import matplotlib.pyplot as plt


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
granularity = 25
veh1 = reader.load_one_row(filepath, 324, granularity)
print(veh1)

veh2 = reader.load_one_row(filepath, 6, granularity)
print(veh2)

timeList = []
distanceList = []
speedList = []
for i in range(len(veh1.datas_list)):
    time = veh1.datas_list[i].time
    sep = "."
    rest = time.split(sep, 1)[0]
    rest = str((float(rest) / 1000))
    timeList.append(rest)
    dist = utils.get_distance(veh1.datas_list, i)
    distanceList.append(dist)
    speed = dist / (float(veh1.datas_list[i].time) - float(veh1.datas_list[i-1].time))
    if speed == -0.0:
            speed = 0
    speedList.append(speed)

timeList2 = []
distanceList2 = []
speedList2 = []

for i in range(len(veh2.datas_list)):
    time = veh2.datas_list[i].time
    sep = "."
    rest = time.split(sep, 1)[0]
    rest = str((float(rest) / 1000))
    timeList2.append(rest)
    dist = utils.get_distance(veh2.datas_list, i)
    distanceList2.append(dist)
    speed = dist / (float(veh2.datas_list[i].time) - float(veh2.datas_list[i - 1].time))
    if speed == -0.0:
        speed = 0
    speedList2.append(speed)



plt.figure(1)
fig, ax = plt.subplots()
plt.scatter(timeList, distanceList, s=10, c=distanceList)
plt.plot(timeList, distanceList, label="vehicle67", c='r', linewidth=0.5)
plt.legend()

plt.ylabel("distance")
plt.gcf().autofmt_xdate()
plt.title('distance[m] vs time plot[s]')
cbar = plt.colorbar()
cbar.set_label("distance (m)")
every_nth = 4
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

plt.show()


