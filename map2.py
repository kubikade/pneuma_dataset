import gmplot
import reader


vehicle = reader.load_one_row("pneuma_sample_dataset/pneuma_sample_dataset.csv", 324, 25)
print(vehicle)

lons = []
lats = []

centerLon = (float(vehicle.findMinLon()) + float(vehicle.findMaxLon())) / 2
centerLat = (float(vehicle.findMinLat()) + float(vehicle.findMaxLat())) / 2

for i in range(len(vehicle.datas_list)):
    lons.append(float(vehicle.datas_list[i].lon))
    lats.append(float(vehicle.datas_list[i].lat))

gmap = gmplot.GoogleMapPlotter(centerLat, centerLon, 17)

gmap.scatter(lats, lons, '#00FF00', size=3, marker=False)
gmap.plot(lats, lons, 'blue', edge_width=2.5)

# Pass the absolute path
gmap.draw("map.html")

