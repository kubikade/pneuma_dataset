
class Vehicle:
    def __init__(self, track_id, type, traveled_distance, avg_speed, datas_list):
        self.track_id = track_id
        self.type = type
        self.traveled_distance = traveled_distance
        self.avg_speed = avg_speed
        self.datas_list = datas_list

    def __str__(self):
        ret = "Vehicle{" + self.track_id + "; " + self.type + "; " + self.traveled_distance + "; " + self.avg_speed + "; "
        length = len(self.datas_list)
        for x in range(length):
            ret += (str(self.datas_list[x])) + "; "
        ret += "}"
        return ret

    def __repr__(self):
        ret = "{" + self.track_id + "; " + self.type + "; " + self.traveled_distance + "; " + self.avg_speed + "; "
        length = len(self.datas_list)
        for x in range(length):
            ret += (repr(self.datas_list[x])) + "; "
        ret += "}"
        return ret


    def findMinMaxLat(self):
        maxLat = self.datas_list[0].lat
        minLat = self.datas_list[0].lat
        for x in range(len(self.datas_list)):
            if maxLat < self.datas_list[x].lat:
                maxLat = self.datas_list[x].lat
            if minLat > self.datas_list[x].lat:
                minLat = self.datas_list[x].lat
        return (minLat, maxLat)

    def findMinLat(self):
        minLat = self.datas_list[0].lat
        for x in range(len(self.datas_list)):
            if minLat > self.datas_list[x].lat:
                minLat = self.datas_list[x].lat
        return minLat

    def findMaxLat(self):
        maxLat = self.datas_list[0].lat
        for x in range(len(self.datas_list)):
            if maxLat < self.datas_list[x].lat:
                maxLat = self.datas_list[x].lat
        return maxLat

    def findMinMaxLon(self):
        maxLon = self.datas_list[0].lon
        minLon = self.datas_list[0].lon
        for x in range(len(self.datas_list)):
            if maxLon < self.datas_list[x].lon:
                maxLon = self.datas_list[x].lon
            if minLon > self.datas_list[x].lon:
                minLon = self.datas_list[x].lon
        return (minLon, maxLon)

    def findMinLon(self):
        minLon = self.datas_list[0].lon
        for x in range(len(self.datas_list)):
            if minLon > self.datas_list[x].lon:
                minLon = self.datas_list[x].lon
        return minLon

    def findMaxLon(self):
        maxLon = self.datas_list[0].lon
        for x in range(len(self.datas_list)):
            if maxLon < self.datas_list[x].lon:
                maxLon = self.datas_list[x].lon
        return maxLon


class Veh_data:
    def __init__(self, lat, lon, speed, tan_accel, lat_accel, time):
        self.lat = lat
        self.lon = lon
        self.speed = speed
        self.tan_accel = tan_accel
        self.lat_accel = lat_accel
        self.time = time

    def __str__(self):
        return "Data[" + self.lat + ", " + self.lon + ", " + self.speed + ", " + self.tan_accel + ", " + self.lat_accel + ", " + self.time + "]"

    def __repr__(self):
        return "[" + self.lat + ", " + self.lon + ", " + self.speed + ", " + self.tan_accel + ", " + self.lat_accel + ", " + self.time + "]"

