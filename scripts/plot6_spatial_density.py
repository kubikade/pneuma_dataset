import copy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import reader_pandas
import reader


def density_map(latitudes, longitudes, center, bins=550, radius=0.0033):
    cmap = copy.copy(plt.cm.jet)
    cmap.set_bad((0, 0, 0))  # Fill background with black

    # Center the map around the provided center coordinates
    histogram_range = [
        [center[1] - radius, center[1] + radius],
        [center[0] - radius, center[0] + radius]
    ]

    fig = plt.figure(figsize=(20, 20))
    plt.hist2d(longitudes, latitudes, bins=bins, norm=LogNorm(),
               cmap=cmap, range=histogram_range)

    # Remove all axes and annotations to keep the map clean and simple
    plt.grid('off')
    plt.axis('off')

    fig.axes[0].get_xaxis().set_visible(False)
    fig.axes[0].get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
    loaded_vehicles = reader.load_multiple_rows(filepath, 2478)
    df = reader_pandas.create_df(loaded_vehicles)
    gdf = reader_pandas.create_gdf_for_spatial(df)
    all_coordinates = np.array(gdf['coords'].values.tolist())

    center = (37.99109, 23.73347)
    # Separate the latitude and longitude values from our list of coordinates
    latitudes = all_coordinates[:, 0]
    longitudes = all_coordinates[:, 1]
    # Render the map
    density_map(latitudes, longitudes, center=center)
