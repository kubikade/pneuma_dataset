import pandas as pd
import geopandas as gpd
from copy import deepcopy

import reader

# DataFrame column names, track_id will serve as index, not as column name
DF_COLUMN_NAMES = ['type', 'traveled_distance', 'avg_speed', 'lat', 'lon', 'speed', 'tan_acc', 'lat_acc', 'time', 'track_id']
GDF_COLUMN_NAMES = ['track_id', 'speed', 'time', 'geometry']

def gen_df_entry_of_vehicle(veh):
    """gen_df_entry_of_vehicle.
    Args:
        veh: object of Vehicle type.
    Returns:
        track_id: index for new DataFrame entry
        dict: representation of Vehicle type to be appended into DataFrame
    """
    veh_dict = {DF_COLUMN_NAMES[0]: veh.type,
                DF_COLUMN_NAMES[1]: veh.traveled_distance,
                DF_COLUMN_NAMES[2]: veh.avg_speed,
                DF_COLUMN_NAMES[3]: veh.lat_list,
                DF_COLUMN_NAMES[4]: veh.lon_list,
                DF_COLUMN_NAMES[5]: veh.speed_list,
                DF_COLUMN_NAMES[6]: veh.tan_accel_list,
                DF_COLUMN_NAMES[7]: veh.lat_accel_list,
                DF_COLUMN_NAMES[8]: veh.time_list,
                DF_COLUMN_NAMES[9]: veh.track_id
                }
    return veh.track_id, veh_dict


def create_df(loaded_vehicles):
    """create_df.
    Args:
        loaded_vehicles: list of objects of Vehicle type
    Returns:
        df: pandas.DataFrame object.
            rows are indexed with Vehicle.track_id
            columns represent attributes of Vehicle type (Vehicle.type etc.)
    """
    df = pd.DataFrame(columns=DF_COLUMN_NAMES)
    for veh in loaded_vehicles:
        veh_idx, veh_dict = gen_df_entry_of_vehicle(veh)
        df.loc[veh_idx] = veh_dict
    return df


def create_gdf_from_one_entry(df_veh):
    """create_gdf_from_one_entry.
    Creates GeoDataFrame from one row of DataFrame holding Vehicles.
    Args:
        df_veh: pandas.Series object, obtained by df.iloc[x]
    Returns:
        gdf: geopandas.GeoDataFrame containing colums 'time' and 'geometry'.
    """
    gdf = gpd.GeoDataFrame(
            columns=[DF_COLUMN_NAMES[9], DF_COLUMN_NAMES[5], DF_COLUMN_NAMES[8]],  # name the columns
            geometry=gpd.points_from_xy(df_veh.lon, df_veh.lat),
            crs="EPSG:4326")  # not sure about 'crs' argument
    gdf = gdf.assign(track_id=df_veh[DF_COLUMN_NAMES[9]])
    gdf = gdf.assign(speed=df_veh[DF_COLUMN_NAMES[5]])
    gdf = gdf.assign(time=df_veh[DF_COLUMN_NAMES[8]])
    return gdf


def create_gdf(df, veh_ids):
    """create_gdf.
        Creates GeoDataFrame of Vehicles.
        Args:
            df: pandas.DataFrame object with all stored data
            veh_ids: list of VehicleIDs to select Vehicles for GeoDataFrame
        Returns:
            gdf: geopandas.GeoDataFrame containing colums 'track_id', 'speed', 'time' and 'geometry'.
        """
    gdf = create_gdf_from_one_entry(df.iloc[veh_ids[0]])
    for i in range(len(veh_ids)-1):
        gdf = gdf.append(create_gdf_from_one_entry((df.iloc[veh_ids[i+1]])))
    return gdf


if __name__ == '__main__':
    # filepath = "pneuma_sample_dataset/pneuma_sample_dataset_4_entries.csv"
    filepath = "pneuma_sample_dataset/pneuma_sample_dataset.csv"
    loaded_vehicles = reader.load_multiple_rows(filepath, 10)
    df = create_df(loaded_vehicles)
    print(df)
    print(len(df))
    print('---')

    # how to access single entry:
    print('---')
    print(df.iloc[0])

    # how to access the data of single entry
    print('---')
    print(df.iloc[0]['lon'][1])

    print('---gdf:')
    gdf = create_gdf_from_one_entry(df.iloc[7])
    print(gdf)

    gdfc = create_gdf(df, [1, 2, 7])
    print(gdfc)
    print("----")




