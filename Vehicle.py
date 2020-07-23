
class Vehicle:
    def __init__(self, track_id, type, traveled_distance, avg_speed, lat_list, lon_list, speed_list, tan_accel_list, lat_accel_list, time_list):
        self.track_id = track_id
        self.type = type
        self.traveled_distance = traveled_distance
        self.avg_speed = avg_speed
        self.lat_list = lat_list
        self.lon_list = lon_list
        self.speed_list = speed_list
        self.tan_accel_list = tan_accel_list
        self.lat_accel_list = lat_accel_list
        self.time_list = time_list

    def __str__(self):
        ret = "Vehicle{" + self.track_id + "; " + self.type + "; " + self.traveled_distance + "; " + self.avg_speed + "; "
        length = len(self.lat_list)
        for i in range(length):
            ret += "Data[lat: " + str(self.lat_list[i]) + ", lon: " + str(self.lon_list[i]) + ", speed: " + str(self.speed_list[i]) + ", tan_acc: " + str(self.tan_accel_list[i]) + ", lat_acc: " + str(self.lat_accel_list[i]) + ", time: " + str(self.time_list[i]) + "]; "
        ret += "}"
        return ret

    def __repr__(self):
        ret = "{" + self.track_id + "; " + self.type + "; " + self.traveled_distance + "; " + self.avg_speed + "; "
        length = len(self.lat_list)
        for i in range(length):
            ret += "[lat: " + str(self.lat_list[i]) + ", lon: " + str(self.lon_list[i]) + ", speed: " + str(self.speed_list[i]) + ", tan_acc: " + str(self.tan_accel_list[i]) + ", lat_acc: " + str(self.lat_accel_list[i]) + ", time: " + str(self.time_list[i]) + "]; "
        ret += "}"
        return ret

    def findMinMaxLat(self):
        maxLat = max(self.lat_list)
        minLat = min(self.lat_list)
        return minLat, maxLat

    def findMinLat(self):
        minLat = min(self.lat_list)
        return minLat

    def findMaxLat(self):
        maxLat = max(self.lat_list)
        return maxLat

    def findMinMaxLon(self):
        maxLon = max(self.lon_list)
        minLon = min(self.lon_list)
        return minLon, maxLon

    def findMinLon(self):
        minLon = min(self.lon_list)
        return minLon

    def findMaxLon(self):
        maxLon = max(self.lon_list)
        return maxLon


"""
class VehData:
    def __init__(self, lat, lon, speed, tan_accel, lat_accel, time):
        self.lat = lat
        self.lon = lon
        self.speed = speed
        self.tan_accel = tan_accel
        self.lat_accel = lat_accel
        self.time = time

    def __str__(self):
        return "Data[lat: " + self.lat + ", lon: " + self.lon + ", speed: " + self.speed + ", tan_acc: " + self.tan_accel + ", lat_acc: " + self.lat_accel + ", time: " + self.time + "]"

    def __repr__(self):
        return "[lat: " + self.lat + ", lon: " + self.lon + ", speed: " + self.speed + ", tan_acc: " + self.tan_accel + ", lat_acc: " + self.lat_accel + ", time: " + self.time + "]"    
"""

