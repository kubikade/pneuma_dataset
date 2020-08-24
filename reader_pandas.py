import pandas as pd
import geopandas as gpd

# DataFrame column names, track_id will serve as index, not as column name
DF_COLUMN_NAMES = ['type', 'traveled_distance', 'avg_speed', 'lat', 'lon', 'speed', 'tan_acc', 'lat_acc', 'time']


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
        gdf: geopandas.GeoDataFrame containing columns 'time' and 'geometry'.
    """
    gdf = gpd.GeoDataFrame(
            columns=['track_id', DF_COLUMN_NAMES[5], DF_COLUMN_NAMES[8]],  # name the columns
            geometry=gpd.points_from_xy(df_veh.lon, df_veh.lat),
            crs="EPSG:4326")  # not sure about 'crs' argument
    gdf = gdf.assign(track_id=df_veh.name)
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
            gdf: geopandas.GeoDataFrame containing columns 'track_id', 'speed', 'time' and 'geometry'.
    """
    gdf = create_gdf_from_one_entry(df.iloc[veh_ids[0]])
    for i in range(len(veh_ids)-1):
        gdf = gdf.append(create_gdf_from_one_entry((df.iloc[veh_ids[i+1]])))
    gdf['time'] = pd.to_datetime(gdf['time'])
    gdf = gdf.set_index('time')
    return gdf


def create_gdf_from_whole_df(df):
    """create_gdf_from_whole_df.
        Creates GeoDataFrame of Vehicles.
        Args:
            df: pandas.DataFrame object with all stored data
        Returns:
            gdf: geopandas.GeoDataFrame containing columns 'track_id', 'speed', 'time' and 'geometry'.
    """
    gdf = create_gdf_from_one_entry(df.iloc[0])
    for i in range(len(df.index)-1):
        gdf = gdf.append(create_gdf_from_one_entry(df.iloc[i + 1]))
    gdf['time'] = pd.to_datetime(gdf['time'])
    gdf = gdf.set_index('time')
    return gdf


def list_to_flat_list(list):
    """list_to_flat_list.
        Creates flat list with data from lists.
        Args:
            list: list of lists with data.
        Returns:
            flat: flat list with data.
    """
    flat = []
    for sublist in list:
        for item in sublist:
            flat.append(item)
    return flat


def create_lists_for_gdf(df):
    """create_lists_for_gdf.
        Creates lists with data for geopandas.GeoDataFrame.
        Args:
            df: pandas.DataFrame object with all stored data
        Returns:
            flat_track_ids, speeds, times, lats, lons: flat lists with data from df columns.
    """
    temp = df[DF_COLUMN_NAMES[5]].tolist()
    speeds = list_to_flat_list(temp)
    times = list_to_flat_list(df[DF_COLUMN_NAMES[8]].tolist())
    lons = list_to_flat_list(df[DF_COLUMN_NAMES[4]].tolist())
    lats = list_to_flat_list(df[DF_COLUMN_NAMES[3]].tolist())
    veh_ids = []
    for i in range(len(df)):
        veh_ids.append([df.index[i]] * len(temp[i]))
    flat_track_ids = list_to_flat_list(veh_ids)
    return flat_track_ids, speeds, times, lats, lons


def create_gdf_using_lists(df):
    """create_gdf_using_lists.
        Creates geopandas.GeoDataFrame from pandas.DataFrame.
        Args:
            df: pandas.DataFrame object with all stored data
        Returns:
            gdf: geopandas.GeoDataFrame containing columns 'track_id', 'speed', 'time' and 'geometry'.
    """
    track_ids, speeds, times, lats, lons = create_lists_for_gdf(df)
    gdf = gpd.GeoDataFrame(
        columns=['track_id', 'speed', 'time'],  # name the columns
        geometry=gpd.points_from_xy(lons, lats),
        crs="EPSG:4326")  # not sure about 'crs' argument
    gdf = gdf.assign(track_id=track_ids)
    gdf = gdf.assign(speed=speeds)
    gdf = gdf.assign(time=times)
    gdf['time'] = pd.to_datetime(gdf['time'])
    gdf = gdf.set_index('time')
    return gdf


def create_gdf_for_spatial(df):
    """create_gdf_using_lists.
        Creates geopandas.GeoDataFrame from pandas.DataFrame.
        Args:
            df: pandas.DataFrame object with all stored data
        Returns:
            gdf: geopandas.GeoDataFrame containing columns 'track_id', 'speed', 'time' and 'geometry'.
    """
    track_ids, speeds, times, lats, lons = create_lists_for_gdf(df)
    gdf = gpd.GeoDataFrame(
        columns=['track_id', 'speed', 'time', 'coords'],  # name the columns
        geometry=gpd.points_from_xy(lons, lats),
        crs="EPSG:4326")  # not sure about 'crs' argument
    geopoints = list(zip(lats, lons))
    gdf = gdf.assign(track_id=track_ids)
    gdf = gdf.assign(speed=speeds)
    gdf = gdf.assign(time=times)
    gdf = gdf.assign(coords=geopoints)
    gdf['time'] = pd.to_datetime(gdf['time'])
    gdf = gdf.set_index('time')
    return gdf
