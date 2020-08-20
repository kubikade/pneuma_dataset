import matplotlib.pyplot as plt
import sys
sys.path.append("..")
import warnings
warnings.simplefilter("ignore")
import reader
import reader_pandas
import contextily as ctx


filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
loaded_vehicles = reader.load_multiple_rows(filepath, 250)

df = reader_pandas.create_df(loaded_vehicles)
gdf = reader_pandas.create_gdf_using_lists(df)
gdf = gdf.to_crs(epsg=3857)

ax = gdf.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

plt.show()
