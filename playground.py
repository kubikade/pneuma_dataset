import urllib
import os
import numpy as np
import pandas as pd
from geopandas import GeoDataFrame, read_file
from shapely.geometry import Point, LineString, Polygon
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

import sys
sys.path.append("..")
import movingpandas as mpd

import warnings
warnings.simplefilter("ignore")

import reader
import reader_pandas

filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
loaded_vehicles = reader.load_multiple_rows(filepath, 20)
all = []
for i in range(20):
  all.append(i)

df = reader_pandas.create_df(loaded_vehicles)
gdf = reader_pandas.create_gdf(df, all)

gdf['time'] = pd.to_datetime(gdf['time'])
gdf = gdf.set_index('time')

MIN_LENGTH = 100 # meters
traj_collection = mpd.TrajectoryCollection(gdf, 'track_id', min_length=MIN_LENGTH)
print("Finished creating {} trajectories".format(len(traj_collection)))

traj_collection.plot()

plt.show()
