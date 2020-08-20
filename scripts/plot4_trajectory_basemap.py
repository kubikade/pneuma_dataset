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
import contextily as ctx


filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
loaded_vehicles = reader.load_multiple_rows(filepath, 200)

poly = Polygon([(23.73459, 37.99090), (23.73444, 37.99020), (23.73468, 37.99090), (23.73450, 37.99032)])
poly2 = Polygon([(23.73250, 37.99112), (23.73250, 37.99104), (23.73456, 37.99079), (23.73456, 37.99071)])

filtered = utils.veh_pass_through_polygons(loaded_vehicles, [poly, poly2])
print("Found {} intersections".format(len(filtered)))

df = reader_pandas.create_df(filtered)
gdf = reader_pandas.create_gdf_using_lists(df)
gdf = gdf.to_crs(epsg=3857)

traj_collection = mpd.TrajectoryCollection(gdf, 'track_id')

ax = traj_collection.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

plt.show()
