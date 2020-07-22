import pandas as pd

import reader

# DataFrame column names, track_id will serve as index, not as column name
DF_COLUMN_NAMES = ['type_id', 'traveled_distance', 'avg_speed', 'repeated_data']


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
                DF_COLUMN_NAMES[3]: veh.datas_list
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


if __name__ == '__main__':
    filepath = "pneuma_sample_dataset/pneuma_sample_dataset_4_entries.csv"
    loaded_vehicles = reader.load_multiple_rows(filepath, 4)
    df = create_df(loaded_vehicles)
    print(df)

    # how to access single entry:
    print('---')
    print(df.iloc[0])

    # how to access the data of single entry
    print('---')
    print(df.iloc[0]['repeated_data'][1])

