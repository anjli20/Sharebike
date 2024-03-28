# initialize.py

    create the database locally and insert basic test data
    show some examples of the data structure in the console

# enum_values.py

    includes all the enum values,
    including vehicle status and user type

# general.py

    when register or sign in, make sure to use enum_values.UserType.USERTYPE.value

    register and sign in
    the register process is different for customer(sign_up),
    manager(sign_up_inner) and employee(sign_up_inner)

# customer.py

    when change status of vehicles, make sure to use enum_values.Status.STATUS.value

    rent(vehicle_id, time, location_id, cust_id)---if success return True, else return False

    returnBike(vehicle_id, time, location_id, cust_id)---if success return True, else return False

    report(vehicle_id, time, status, location_id)---change the status, use the enum_values.Status.STATUS.value
    
    history(cust_id)---get all the travel information of a single customer
    return a list of series containing all trips of a customer

        history(1)[0]---the first travel information of customer1

        trip_id                         1.0
        vehicle_id                      1.0
        start_time                     12.0
        end_time                       15.0
        charge                          9.0
        start_station_name    station_name1
        start_postcode            postcode1
        end_station_name      station_name3
        end_postcode              postcode3

# manager.py

    report_single(vehicle_id)---get all the travel information of a single vehicle
    return a list of series of travel information of a single vehicle

        report_single(1)[0]---the first travel information of vehicle1

        info_id                     1
        time                        1
        status                 RENTED
        station_name    station_name1
        postcode            postcode1

    report_all()---get all the travel information of all vehicles
    return a dictonary, the keys are vehilce id, values are lists of series of travel information

        report_all()[1][0]---the first travel information of vehicle1

        info_id                     1
        time                        1
        status                 RENTED
        station_name    station_name1
        postcode            postcode1

    report_period(start_time, end_time)---get the travel information of all vehicles during a period of time
    return a dictonary, the keys are vehilce id, values are lists of series of travel information

        report_all()[1][0]---the first travel information of vehicle1

        info_id                     1
        time                        1
        status                 RENTED
        station_name    station_name1
        postcode            postcode1

# employee.py

    when change status of vehicles, make sure to use enum_values.Status.STATUS.value

    get_locations()---get all the locations
    return a list of series of information of locations

        get_locations()[0]

        location_id                 1
        station_name    station_name1
        postcode            postcode1

    track()---get all the latest information of all vehicles
    return a dictionary, keys are vehicle ids, values are a series of information

        track()[1]---the latest information of vehicle1

        info_id                     3
        time                       12
        status               LOWPOWER
        station_name    station_name2
        postcode            postcode2

    track_charge()---get all the latest information of  vehicles which are low power
    return a dictionary, keys are vehicle ids, values are a series of information

        track()[1]---the latest information of vehicle1

        info_id                     3
        time                       12
        status               LOWPOWER
        station_name    station_name2
        postcode            postcode2

    charge(vehicle_id, time, location_id)---if success return True, else return False

    track_repair()---get all the latest information of  vehicles which are broken
    return a dictionary, keys are vehicle ids, values are a series of information

        track()[1]---the latest information of vehicle1

        info_id                     3
        time                       12
        status               LOWPOWER
        station_name    station_name2
        postcode            postcode2

    repair(vehicle_id, time, location_id)---if success return True, else return False

    move(vehicle_id, time, location_id)---move vehicles to location_id

    move_with_name(vehicle_id, time, station_name)---move vehicles to station_name
