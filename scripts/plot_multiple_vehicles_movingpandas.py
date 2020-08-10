import matplotlib.pyplot as plt
import sys
sys.path.append("..")
import movingpandas as mpd
import warnings
warnings.simplefilter("ignore")
import reader
import reader_pandas


filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
loaded_vehicles = reader.load_multiple_rows(filepath, 20)

df = reader_pandas.create_df(loaded_vehicles)
gdf = reader_pandas.create_gdf_from_whole_df(df)
MIN_LENGTH = 100 # meters
traj_collection = mpd.TrajectoryCollection(gdf, 'track_id', min_length=MIN_LENGTH)
print("Finished creating {} trajectories".format(len(traj_collection)))
traj_collection.plot()

plt.show()