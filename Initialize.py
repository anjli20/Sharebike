# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:17:38 2023

@author: 17393
"""
import random
import time

import dbFun
import enum_values
import customer
import general

manager_num = 1
operator_num = 5
customer_num = 10
vehicle_num = 30
location_num = 10
trip_num = 100
malfunction_num = 5

start_point = int(time.mktime(time.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')))
min_riding_time = 1800
max_riding_time = 7200

dbFun.create_db()

# create locations
for i in range(location_num):
    station = "station" + str(i+1)
    postcode = "postcode" + str(i+1)

    dbFun.create_location(station, postcode)

# create vehicles
for i in range(vehicle_num):
    vehicle_type = random.choice(["E-Bike", "Bike"])
    location_id = random.choice(range(1, location_num+1))

    dbFun.create_vehicle(vehicle_type, location_id, start_point)

# create customers
for i in range(customer_num):
    password = "password" + str(i+1)
    fname = "fname" + str(i+1)
    lname = "lname" + str(i+1)
    email = "email" + str(i+1)
    phnum = "phnum" + str(i+1)
    bank_acc_nbr = "bank_acc_nbr" + str(i+1)

    general.sign_up(password, fname, lname, email, phnum, bank_acc_nbr)

# create operator
for i in range(operator_num):
    password = "password" + str(i+1)
    fname = "fname" + str(i+1)
    lname = "lname" + str(i+1)
    email = "email" + str(i+1)
    phnum = "phnum" + str(i+1)
    bank_acc_nbr = "bank_acc_nbr" + str(i+1)

    general.sign_up_inner(enum_values.UserType.OPERATOR.value, password, fname, lname, email, phnum)

# create manager
for i in range(manager_num):
    password = "password" + str(i+1)
    fname = "fname" + str(i+1)
    lname = "lname" + str(i+1)
    email = "email" + str(i+1)
    phnum = "phnum" + str(i+1)
    bank_acc_nbr = "bank_acc_nbr" + str(i+1)

    general.sign_up_inner(enum_values.UserType.MANAGER.value, password, fname, lname, email, phnum)

# create trip
for i in range(trip_num):
    cust_id = random.choice(range(1, customer_num + 1))
    vehicle_id = random.choice(range(1, vehicle_num+1))

    start_location_id = random.choice(range(1, location_num+1))

    end_point = start_point + random.randint(min_riding_time, max_riding_time)
    end_location_id = random.choice(range(1, location_num + 1))

    customer.rent(vehicle_id, start_location_id, cust_id, start_point)
    customer.returnBike(vehicle_id, end_location_id, cust_id, end_point)

    start_point = end_point

# report malfunction
for i in range(malfunction_num):
    vehicle_id = random.choice(range(1, vehicle_num+1))
    if dbFun.get_type(vehicle_id) == "E-Bike":
        status = random.choice([enum_values.Status.LOWPOWER.value, enum_values.Status.BROKEN.value])
    else:
        status = enum_values.Status.BROKEN.value
    location_id = random.choice(range(1, location_num+1))

    customer.report(vehicle_id, status, location_id)

for i in range(vehicle_num):
    if dbFun.check_status(i + 1) != "VACANT":
        print("vehicle" + str(i + 1) + ": " + dbFun.check_status(i + 1))

# dbFun.create_vehicle("E-Bike", 1)
# dbFun.create_vehicle("Bike", 2)
# dbFun.create_vehicle("Bike", 3)
#
# dbFun.create_location("station_name1", "postcode1")
# dbFun.create_location("station_name2", "postcode2")
# dbFun.create_location("station_name3", "postcode3")

# general.sign_up("password1", "fname1", "lname1", "email1", "phnum1", "bank_acc_nbr1")
# general.sign_up("password2", "fname2", "lname2", "email2", "phnum2", "bank_acc_nbr2")
# general.sign_up("password3", "fname3", "lname3", "email3", "phnum3", "bank_acc_nbr3")

# customer1 travel from location1 to location3 with vehicle1
# customer.rent(1, 1, 1)
# customer.returnBike(1, 3, 1)
# # report low power
# customer.report(1, enum_values.Status.LOWPOWER.value, 3)
# # customer1 pay 3 pounds
# customer.pay(1, 3)
# # check the trip history of customer1
# print("customer1 travel history:")
# data = customer.history(1)
# for item in data:
#     print(item)
#
# print()
# # operator charge the bike, move it to location2
# employee.charge(1, 3)
# employee.move(1, 2)
# # track the latest information of all vehicles
# print("employee track:")
# data = employee.track()
# for item in data.items():
#     print("vehicle" + str(item[0]))
#     print(item[1])
#
# print()
# # manager check all the information of all vehicles
# print("manager report:")
# data = manager.report_all()
# for item in data.items():
#     print("vehicle" + str(item[0]))
#     for element in item[1]:
#         print(element)
#     print()
#
# print()
# # manager check the information of all vehicles during a period
# print("manager period report:")
# data = manager.report_period("2023-10-24 15:30", "2023-10-24 16:30")
# for item in data.items():
#     print("vehicle" + str(item[0]))
#     for element in item[1]:
#         print(element)
#     print()
