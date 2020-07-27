import pandas as pd
from shapely import wkt
from shapely.geometry import Point
import reader
from geopandas import GeoDataFrame
import geopandas

# DataFrame column names, track_id will serve as index, not as column name
DF_COLUMN_NAMES = ['type_id', 'traveled_distance', 'avg_speed', 'lat', 'lon', 'speed', 'tan_acc', 'lat_acc', 'time']


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
                DF_COLUMN_NAMES[8]: veh.time_list
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


def to_gdf(df):
    gdf = GeoDataFrame(
        df, geometry=geopandas.points_from_xy(df.iloc[0]['lon'], df.iloc[0]['lat']))
    return gdf


if __name__ == '__main__':
    filepath = "pneuma_sample_dataset/pneuma_sample_dataset_4_entries.csv"
    loaded_vehicles = reader.load_multiple_rows(filepath, 1)
    df = create_df(loaded_vehicles)
    print(df)
    print(len(df))

    print('---------')
    gdf = to_gdf(df)
    print(gdf)

    # how to access single entry:
    print('---')
    print(df.iloc[0])

    # how to access the data of single entry
    print('---')
    print(df.iloc[0]['lon'][1])

