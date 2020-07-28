import gmplot


def to_map_plot(vehicles, filename="map.html"):
    """to_map_plot.

    Creates map plot with trajectories of vehicles.

    Args:
         vehicles: list of Vehicle type objects
         filename: name of a html file with map plot
    """
    centerLon = (float(vehicles[0].findMinLon()) + float(vehicles[0].findMaxLon())) / 2
    centerLat = (float(vehicles[0].findMinLat()) + float(vehicles[0].findMaxLat())) / 2
    gmap = gmplot.GoogleMapPlotter(centerLat, centerLon, 17)
    for vehicle in vehicles:
        gmap.scatter(vehicle.lat_list, vehicle.lon_list, '#00FF00', size=3, marker=False)
        gmap.plot(vehicle.lat_list, vehicle.lon_list, 'blue', edge_width=2.5)
    gmap.draw(filename)

