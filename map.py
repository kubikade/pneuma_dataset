import gmplot
import reader

granularity = 25
carnumbers = 279, 234, 444
vehicles = []

for i in carnumbers:
    vehicle = reader.load_one_row("pneuma_sample_dataset/pneuma_sample_dataset.csv", i+1, granularity)
    print(vehicle)
    vehicles.append(vehicle)

centerLon = (float(vehicle.findMinLon()) + float(vehicle.findMaxLon())) / 2
centerLat = (float(vehicle.findMinLat()) + float(vehicle.findMaxLat())) / 2
gmap = gmplot.GoogleMapPlotter(centerLat, centerLon, 17)

for vehicle in vehicles:
    lons = []
    lats = []
    for i in range(len(vehicle.datas_list)):
        lons.append(float(vehicle.datas_list[i].lon))
        lats.append(float(vehicle.datas_list[i].lat))
    gmap.scatter(lats, lons, '#00FF00', size=3, marker=False)
    gmap.plot(lats, lons, 'blue', edge_width=2.5)

gmap.draw("map.html")

