import gmplot
import reader
import utils

granularity = 25
carnumbers = 1794, 1805, 1819, 1825, 1836, 1855
vehicles = []


"""for i in carnumbers:
    vehicle = reader.load_one_row("pneuma_sample_dataset/pneuma_sample_dataset.csv", i+1, granularity)
    print(vehicle)
    vehicles.append(vehicle)"""

filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
BBox = [37.98948, 37.99054, 23.73059, 23.73113]

BBoxleft = [37.99130, 37.99163, 23.73236, 23.73326]
BBoxright = [37.99083, 37.99102, 23.73559, 23.73694]
BBoxdown = [37.99134, 37.99157, 23.72996, 23.73061]

vehicles = reader.load_rows_in_interval(filepath, 1, 555, granularity)
ll = utils.pass_through_BBox(vehicles, *BBoxleft)
rr = utils.pass_through_BBox(ll, *BBoxright)
dep = utils.pass_through_BBox(rr, *BBoxdown)

centerLon = (float(dep[0].findMinLon()) + float(dep[0].findMaxLon())) / 2
centerLat = (float(dep[0].findMinLat()) + float(dep[0].findMaxLat())) / 2
gmap = gmplot.GoogleMapPlotter(centerLat, centerLon, 17)

for vehicle in dep:
    print(vehicle)
    lons = []
    lats = []
    for i in range(len(vehicle.datas_list)):
        lons.append(float(vehicle.datas_list[i].lon))
        lats.append(float(vehicle.datas_list[i].lat))
    gmap.scatter(lats, lons, '#00FF00', size=3, marker=False)
    gmap.plot(lats, lons, 'blue', edge_width=2.5)

gmap.draw("map.html")

