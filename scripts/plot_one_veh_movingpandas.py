"""

author: Obrusnik Vit
"""
import sys
sys.path.append('.')

import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame, read_file
from shapely.geometry import Point, LineString, Polygon
from fiona.crs import from_epsg
from datetime import datetime, timedelta
from matplotlib import pyplot as plt

import movingpandas as mpd
print(mpd.__version__)

# our imports
import reader
import reader_pandas

def main():
    print("start!")
    filepath = "pneuma_sample_dataset/pneuma_sample_dataset_4_entries.csv"
    loaded_vehicles = reader.load_multiple_rows(filepath, 4)
    df = reader_pandas.create_df(loaded_vehicles)

    gdf1 = reader_pandas.create_gdf_from_one_entry(df.iloc[0])
    gdf2 = reader_pandas.create_gdf_from_one_entry(df.iloc[1])

    traj1 = mpd.Trajectory(gdf1, 1)
    traj2 = mpd.Trajectory(gdf2, 2)

    fig, ax = plt.subplots()
    traj1.plot(ax=ax, linewidth=2, capstyle='round', legend=True)
    traj2.plot(ax=ax, linewidth=2, capstyle='round', legend=True, color='r')
    plt.show()

    print("done!")


if __name__ == '__main__':
    main()

