import gmplot
import reader
import utils

granularity = 25
vehicles = []

filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"

BBoxleft = [37.99130, 37.99163, 23.73236, 23.73326]
BBoxright = [37.99083, 37.99102, 23.73559, 23.73694]
BBoxdown = [37.99134, 37.99157, 23.72996, 23.73061]

vehicles = reader.load_rows_in_interval(filepath, 1, 150, granularity)
ll = utils.pass_through_BBox(vehicles, *BBoxleft)
rr = utils.pass_through_BBox(ll, *BBoxright)
dep = utils.pass_through_BBox(rr, *BBoxdown)
"""
vehicle = reader.load_one_row(filepath, 65, granularity)
dep = []
dep.append(vehicle)
"""

centerLon = (float(dep[0].findMinLon()) + float(dep[0].findMaxLon())) / 2
centerLat = (float(dep[0].findMinLat()) + float(dep[0].findMaxLat())) / 2
gmap = gmplot.GoogleMapPlotter(centerLat, centerLon, 17)

for vehicle in dep:
    print(vehicle)
    gmap.scatter(vehicle.lat_list, vehicle.lon_list, '#00FF00', size=3, marker=False)
    gmap.plot(vehicle.lat_list, vehicle.lon_list, 'blue', edge_width=2.5)

gmap.draw("map.html")

