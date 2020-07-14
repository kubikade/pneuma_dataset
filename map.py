import matplotlib.pyplot as plt
import reader


vehicle = reader.load_one_row("pneuma_sample_dataset/pneuma_sample_dataset.csv", 324, 100)
print(vehicle)

lons = []
lats = []

BBox = (float(vehicle.findMinLon()), float(vehicle.findMaxLon()), float(vehicle.findMinLat()), float(vehicle.findMaxLat()))

for i in range(len(vehicle.datas_list)):
    lons.append(float(vehicle.datas_list[i].lon))
    lats.append(float(vehicle.datas_list[i].lat))

mapimg = plt.imread("map.png")

fig, ax = plt.subplots(figsize=(8, 7))
for j in range(len(vehicle.datas_list)):
    ax.scatter(lons, lats, zorder=1, alpha= 0.2, c='b', s=10)
    ax.set_title('')
    ax.set_xlim(float(vehicle.findMinLon()), float(vehicle.findMaxLon()))
    ax.set_ylim(float(vehicle.findMinLat()), float(vehicle.findMaxLat()))
ax.imshow(mapimg, zorder=0, extent=BBox, aspect='equal')
plt.show()
