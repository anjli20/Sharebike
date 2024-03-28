import dbFun
import pandas as pd
import time
import enum_values


def get_locations():
    data = dbFun.get_locations()
    result = []
    for item in data:
        series = pd.Series(item, index=["location_id", "station_name", "postcode"])
        result.append(series)
    return result


def track():
    # {1: (3, 12, 'LOWPOWER', 2),
    # 2: (3, 12, 'LOWPOWER', 2),
    # 3: (3, 12, 'LOWPOWER', 2),
    # 4: (2, 18, 'VACANT', 2)}
    data = dbFun.get_latest_vehicleInfos()
    result = {}
    for item in data.items():
        series = pd.Series(item[1], index=['info_id', 'time', 'status', 'location_id'])

        location = dbFun.get_loc_name(series['location_id'])
        series['station_name'] = location[0][0]
        series['postcode'] = location[0][1]
        series = series.drop("location_id")

        time_stamp = series['time']
        time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(time_stamp))
        series['time'] = time_str

        result[item[0]] = series
    return result


def track_charge():
    data = track()
    result = {}
    for items in data.items():
        if items[1]["status"] == enum_values.Status.LOWPOWER.value:
            result[items[0]] = items[1]
    return result


def charge(vehicle_id, location_id):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.LOWPOWER.value:
        status = enum_values.Status.VACANT.value
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, status, location_id)

        return True
    else:
        return False


def track_repair():
    data = track()
    result = {}
    for items in data.items():
        if items[1]["status"] == enum_values.Status.BROKEN.value:
            result[items[0]] = items[1]
    return result


def repair(vehicle_id, location_id):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.BROKEN.value:
        status = enum_values.Status.VACANT.value
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, status, location_id)

        return True
    else:
        return False


def move(vehicle_id, location_id):
    status = enum_values.Status.VACANT.value
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, status, location_id)


def move_with_name(vehicle_id, station_name):
    status = enum_values.Status.VACANT.value
    location_id = dbFun.get_loc_id(station_name)
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, status, location_id)


def track_vehicle():
    # vehicle_dtl = dbFun.track_vehicle_database()
    # for i in vehicle_dtl:
    #     print (i[1])

    test = dbFun.get_vehicleInfos()
    vehicles_status = {}
    all_loc_dict = fetch_all_location_info_in_dict()
    for i in range(1,len(test)+1):
        time = 0
        for j in test[i]:
            if j[1] > time:
                time = j[1]
                formatted_info = [j[0],j[1],j[2],all_loc_dict[j[3]]]
                vehicles_status.update({i: formatted_info})
    return vehicles_status


def update_vehicle_charge(vehicle_id, time, status, location_id):
    dbFun.insert_vehicleInfo(vehicle_id, status, location_id)


def fetch_all_location_info_in_dict():
    all_loc = dbFun.get_all_loc()
    all_loc_dict = {}
    for row in all_loc:
        all_loc_dict.update({row[0]: row[1]})
    return all_loc_dict


def track_vehicle_with_time(start_time,end_time):
    # vehicle_dtl = dbFun.track_vehicle_database()
    # for i in vehicle_dtl:
    #     print (i[1])

    test = dbFun.get_vehicleInfos()
    vehicles_status = {}
    all_loc_dict = fetch_all_location_info_in_dict()
    for i in range(1,len(test)+1):
        time = 0
        for j in test[i]:
            if j[1] >= start_time and j[1] <= end_time and j[1] > time:
                time = j[1]
                formatted_info = [j[0],j[1],j[2],all_loc_dict[j[3]]]
                vehicles_status.update({i: formatted_info})
    return vehicles_status
