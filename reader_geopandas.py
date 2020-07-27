import pandas as pd
import geopandas
import Vehicle
import csv

# DataFrame column names, track_id will serve as index, not as column name
DF_COLUMN_NAMES = ['track_id', 'type', 'traveled_distance', 'avg_speed', 'lat', 'lon', 'speed', 'tan_acc', 'lat_acc', 'time']


def gen_df_entry_of_vehicle(veh):
    """gen_df_entry_of_vehicle.

    Args:
        veh: object of Vehicle type.

    Returns:
        track_id: index for new DataFrame entry
        dict: representation of Vehicle type to be appended into DataFrame
    """
    veh_dict = {DF_COLUMN_NAMES[0]: veh.track_id,
                DF_COLUMN_NAMES[1]: veh.type,
                DF_COLUMN_NAMES[2]: veh.traveled_distance,
                DF_COLUMN_NAMES[3]: veh.avg_speed,
                DF_COLUMN_NAMES[4]: veh.lat_list,
                DF_COLUMN_NAMES[5]: veh.lon_list,
                DF_COLUMN_NAMES[6]: veh.speed_list,
                DF_COLUMN_NAMES[7]: veh.tan_accel_list,
                DF_COLUMN_NAMES[8]: veh.lat_accel_list,
                DF_COLUMN_NAMES[9]: veh.time_list
                }
    return veh_dict


def create_df(loaded_vehicles):
    """create_df.

    Args:
        loaded_vehicles: list of objects of Vehicle type

    Returns:
        df: pandas.DataFrame object.
            rows are indexed with Vehicle.track_id
            columns represent attributes of Vehicle type (Vehicle.type etc.)
    """
    row = 1
    df = pd.DataFrame(columns=DF_COLUMN_NAMES)
    for veh in loaded_vehicles:
        veh_dict = gen_df_entry_of_vehicle(veh)
        df.loc[row] = veh_dict
        row += 1
    return df


def to_gdf(df):
    gdf = geopandas.GeoDataFrame(
        df, geometry=geopandas.points_from_xy(df.lon, df.lat))
    return gdf


def load_multiple_rows(filepath, nrows, granularity=1):
    number_of_data = 6
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        vehicles = []
        next(reader)
        for i in range(nrows):
            row = []
            temporary = next(reader)
            for val in temporary:
                val = val.replace(" ", "")
                row.append(val)
            vehicle_info = get_Vehicle_info(row)
            offset = i = 4
            while i < len(row)-1:
                lat = (float(row[i]))
                lon = (float(row[i+1]))
                speed = (float(row[i+2]))
                tan_accel = (float(row[i+3]))
                lat_accel = (float(row[i+4]))
                time = (float(row[i+5])/1000)
                i += (number_of_data * granularity)
                vehicle = Vehicle.Vehicle(*vehicle_info, lat, lon, speed, tan_accel, lat_accel, time)
                vehicles.append(vehicle)
        return vehicles


# returns list of first 4 parameters for Vehicle object
def get_Vehicle_info(line):
    ret = []
    number_of_info = 4
    for i in range(number_of_info):
        ret.append(line[i])
    return ret


if __name__ == '__main__':
    filepath = "pneuma_sample_dataset/pneuma_sample_dataset_4_entries.csv"
    loaded_vehicles = load_multiple_rows(filepath, 3)
    df = create_df(loaded_vehicles)
    print(df)

    print('---------')
    gdf = to_gdf(df)
    print(gdf)
