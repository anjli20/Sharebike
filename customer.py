import pandas as pd
import dbFun
import enum_values
import time

charge_policy = {"Bike": 0.1, "E-Bike": 0.2}


def rent(vehicle_id, location_id, cust_id, start_time_stamp=time.time()):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.VACANT.value:
        # create new vehicleInfo, add it to the table
        status = enum_values.Status.RENTED.value
        dbFun.insert_vehicleInfo(vehicle_id, status, location_id, start_time_stamp)
        # create new trip, add it to the table
        dbFun.start_trip(cust_id, vehicle_id, location_id, start_time_stamp)

        return True
    else:
        return False


def returnBike(vehicle_id, location_id, cust_id, end_time_stamp=time.time()):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.RENTED.value:
        start_time_stamp = dbFun.get_time(vehicle_id)
        vehicle_type = dbFun.get_type(vehicle_id)

        # create new vehicleInfo, add it to the table
        status = enum_values.Status.VACANT.value
        dbFun.insert_vehicleInfo(vehicle_id, status, location_id, end_time_stamp)

        # calculate the charge
        period = end_time_stamp - start_time_stamp
        charge = round(period / 1800 * charge_policy.get(vehicle_type), 2)
        balance = round(dbFun.get_balance(cust_id), 2)
        dbFun.update_balance(cust_id, balance - charge)

        # create new trip, add it to the table
        dbFun.end_trip(cust_id, location_id, charge, end_time_stamp)

        return True
    else:
        return False


def report(vehicle_id, status, location_id):
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, status, location_id)


def pay(cust_id, amount):
    balance = dbFun.get_balance(cust_id)
    dbFun.update_balance(cust_id, balance + amount)


# return a list of series containing all trips of a customer
# print(result[0])
#
# trip_id                         1.0
# vehicle_id                      1.0
# start_time                     12.0
# end_time                       15.0
# charge                          9.0
# start_station_name    station_name1
# start_postcode            postcode1
# end_station_name      station_name3
# end_postcode              postcode3
# dtype: object
def history(cust_id):
    trips_list = dbFun.get_trips(cust_id)
    result = []
    for trip in trips_list:
        series = pd.Series(trip, index=['trip_id', 'vehicle_id', 'start_time', 'start_location_id', 'end_time',
                                        'end_location_id', 'charge'])

        start_location = dbFun.get_loc_name(series['start_location_id'])
        series['start_station_name'] = start_location[0][0]
        series['start_postcode'] = start_location[0][1]
        end_location = dbFun.get_loc_name(series['end_location_id'])
        series['end_station_name'] = end_location[0][0]
        series['end_postcode'] = end_location[0][1]

        series = series.drop('start_location_id')
        series = series.drop('end_location_id')

        start_time_stamp = series['start_time']
        start_time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(start_time_stamp))
        series['start_time'] = start_time_str

        end_time_stamp = series['end_time']
        end_time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(end_time_stamp))
        series['end_time'] = end_time_str

        result.append(series)
    return result


def view_profile(cust_id):
    data = dbFun.get_profile(cust_id)
    series = pd.Series(data,
                       index=["cust_id", "bank_acc_nbr", "balance", "password", "fname", "lname", "email", "phnum"])
    return series


def get_local_vehicles(location_id):
    vehicles = dbFun.get_latest_vehicleInfos()
    vehicle_ids = []
    for vehicle_id, vehicles_info in vehicles.items():
        if vehicles_info[3] == location_id:
            vehicle_ids.append(vehicle_id)
    return vehicle_ids
