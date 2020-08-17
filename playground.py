from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

import sys
sys.path.append("..")
import movingpandas as mpd
import warnings
warnings.simplefilter("ignore")
import reader
import reader_pandas
import utils
import geopandas as gpd
import contextily as ctx


filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
loaded_vehicles = reader.load_multiple_rows(filepath, 200)
all = [i for i in range(200)]

poly = Polygon([(23.73459, 37.99090), (23.73444, 37.99020), (23.73468, 37.99090), (23.73450, 37.99032)])
poly4 = Polygon([(23.73250, 37.99112), (23.73250, 37.99104), (23.73456, 37.99079), (23.73456, 37.99071)])

filtered = utils.veh_pass_through_polygons(loaded_vehicles, [poly, poly4])
print("Found {} intersections".format(len(filtered)))


df = reader_pandas.create_df(filtered)
#print(df)

gdf = reader_pandas.create_gdf_using_lists(df)
print(gdf)

"""
MIN_LENGTH = 100 # meters
traj_collection = mpd.TrajectoryCollection(gdf, 'track_id', min_length=MIN_LENGTH)
print("Finished creating {} trajectories".format(len(traj_collection)))
#zaimi street
poly = Polygon([(23.73459, 37.99090), (23.73444, 37.99020), (23.73468, 37.99090), (23.73450, 37.99032)])
#deligianni
poly5 = Polygon([(23.73392, 37.98949), (23.73392, 37.98936), (23.73502, 37.98932), (23.73502, 37.98923)])
# metsovou
poly2 = Polygon([(23.73499, 37.99025), (23.73499, 37.99013), (23.73420, 37.99043), (23.73420, 37.99029)])
# metsovou left
poly3 = Polygon([(23.73217, 37.99069), (23.73217, 37.99055), (23.73359, 37.99051), (23.73359, 37.99035)])
#ioulianou
poly4 = Polygon([(23.73250, 37.99112), (23.73250, 37.99104), (23.73456, 37.99079), (23.73456, 37.99071)])


intersecting = utils.traj_through_polygons(traj_collection, [poly, poly4])
print("Found {} intersections".format(len(intersecting)))
"""
gdf = gdf.to_crs(epsg=3857)

ax = gdf.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

#ax = traj_collection.plot()
plt.show()

# traj_collection.hvplot(geo=True, tiles='OSM', line_width=5, frame_width=300, frame_height=300)
