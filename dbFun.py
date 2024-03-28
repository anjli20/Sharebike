# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:47:06 2023

@author: 17393
"""

import sqlite3
import time

import enum_values


def create_db():
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
            cust_id      INTEGER PRIMARY KEY AUTOINCREMENT
                                  NOT NULL
                                  UNIQUE,
            bank_acc_nbr TEXT,
            balance      REAL,
            password     TEXT,
            fname        TEXT,
            lname        TEXT,
            email        TEXT,
            phnum        TEXT
        );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS managers (
            mana_id  INTEGER PRIMARY KEY AUTOINCREMENT
                              NOT NULL
                              UNIQUE,
            password TEXT,
            fname    TEXT,
            lname    TEXT,
            email    TEXT,
            phnum    TEXT
        );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS operators (
            oper_id  INTEGER PRIMARY KEY AUTOINCREMENT
                              NOT NULL
                              UNIQUE,
            password TEXT,
            fname    TEXT,
            lname    TEXT,
            email    TEXT,
            phnum    TEXT
        );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS locations (
            location_id  INTEGER PRIMARY KEY AUTOINCREMENT
                                  UNIQUE
                                  NOT NULL,
            station_name TEXT,
            postcode     TEXT
        );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS vehicles (
            vehicle_id   INTEGER PRIMARY KEY AUTOINCREMENT
                                  NOT NULL
                                  UNIQUE,
            vehicle_type TEXT
        );""")

    db.close()


def create_customer(password, fname, lname, email, phnum, bank_acc_nbr):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        # sql = """INSERT INTO customers(password, fname, lname, email, phnum, bank_acc_nbr, balance)
        # VALUES (%(password)s,%(fname)s,%(lname)s,%(email)s,%(phnum)s,%(bank_acc_nbr)s,"0.0")"""
        # values = {'password': password, 'fname': fname, 'lname': lname, 'email': email, 'phnum': phnum,
        #           'bank_acc_nbr': bank_acc_nbr}
        # cursor.execute(sql, values)

        sql = "INSERT INTO customers(password, fname, lname, email, phnum, bank_acc_nbr, balance) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"0.0\")".format(
            password, fname, lname, email, phnum, bank_acc_nbr)
        cursor.execute(sql)
        db.commit()

        cust_id = get_num("customers")
        table_name = "trip_" + str(cust_id)
        cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + """ (
            trip_id           INTEGER PRIMARY KEY AUTOINCREMENT
                              UNIQUE
                              NOT NULL,
            vehicle_id        INTEGER REFERENCES vehicles (vehicle_id),
            start_time        REAL,
            start_location_id INTEGER REFERENCES locations (location_id),
            end_time          REAL,
            end_location_id   INTEGER REFERENCES locations (location_id),
            charge            REAL
        );""")
    db.close()


def create_vehicle(vehicle_type, location_id, time_stamp=time.time()):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        # sql = "INSERT INTO vehicles(vehicle_type) VALUES (%(vehicle_type)s)"
        # values = {'vehicle_type': vehicle_type}
        # cursor.execute(sql, values)

        sql = "INSERT INTO vehicles(vehicle_type) VALUES (\"{}\")".format(vehicle_type)
        cursor.execute(sql)
        db.commit()

        vehicle_id = get_num("vehicles")
        table_name = "vehicleInfo_" + str(vehicle_id)
        cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + """ (
            info_id     INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
            time        REAL,
            status      TEXT,
            location_id INTEGER REFERENCES locations (location_id) 
        );""")

        sql = "INSERT INTO " + table_name + "(time, status, location_id) VALUES (\"{}\",\"{}\",\"{}\")".format(
            time_stamp,
            enum_values.Status.VACANT.value,
            location_id)
        cursor.execute(sql)
        db.commit()
    db.close()


def create_location(station_name, postcode):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "INSERT INTO locations(station_name, postcode) VALUES (\"{}\", \"{}\")".format(station_name, postcode)
        cursor.execute(sql)
        db.commit()
    db.close()


def insert_vehicleInfo(vehicle_id, status, location_id, time_stamp=time.time()):
    table_name = "vehicleInfo_" + str(vehicle_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        # sql = "INSERT INTO " + table_name + "(time, status, location_id) VALUES (%(time)d, %(status)s, %(location_id)d)"
        # values = {'time': time, 'status': status, 'location_id': location_id}
        # cursor.execute(sql, values)

        sql = "INSERT INTO " + table_name + "(time, status, location_id) VALUES (\"{}\", \"{}\", \"{}\")".format(
            time_stamp,
            status,
            location_id)
        cursor.execute(sql)
        db.commit()
    db.close()


def start_trip(cust_id, vehicle_id, start_location_id, start_time_stamp):
    table_name = "trip_" + str(cust_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        # sql = "INSERT INTO " + table_name + "(vehicle_id, start_time, start_location_id) VALUES (%(vehicle_id)d, "
        #                                      "%(start_time)d, %(start_location_id)d)"
        # values = {'vehicle_id':vehicle_id,'start_time':start_time,'start_location_id':start_location_id}
        # cursor.execute(sql, values)

        sql = "INSERT INTO " + table_name + "(vehicle_id, start_time, start_location_id) VALUES (\"{}\", \"{}\", \"{}\")".format(
            vehicle_id, start_time_stamp, start_location_id)
        cursor.execute(sql)
        db.commit()
    db.close()


def end_trip(cust_id, end_location_id, charge, end_time_stamp):
    table_name = "trip_" + str(cust_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        # cursor.execute("UPDATE " + table_name + " SET end_time = %d, end_location_id = %d, charge = %f WHERE trip_id = %d",(end_time, end_location_id, charge, trip_id))

        trip_id = get_num(table_name)
        sql = "UPDATE " + table_name + " SET end_time = \"{}\", end_location_id = \"{}\", charge = \"{}\" WHERE trip_id = \"{}\"".format(
            end_time_stamp, end_location_id, charge, trip_id)
        cursor.execute(sql)
        db.commit()
    db.close()


def get_trips(cust_id):
    table_name = "trip_" + str(cust_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM " + table_name
        cursor.execute(sql)
        results = cursor.fetchall()
    db.close()
    return results


def get_latest_trip(cust_id):
    table_name = "trip_" + str(cust_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM " + table_name + " WHERE trip_id = (SELECT MAX(trip_id) FROM " + table_name + ")"
        cursor.execute(sql)
        results = cursor.fetchall()
    db.close()
    return results


def get_vehicleInfo(vehicle_id):
    table_name = "vehicleInfo_" + str(vehicle_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM " + table_name
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result


def get_vehicleInfos():
    vehicle_num = get_num("vehicles")
    results = {}
    for vehicle_id in range(1, vehicle_num + 1):
        results[vehicle_id] = get_vehicleInfo(vehicle_id)
    return results


def get_num(table_name):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT COUNT() FROM {}".format(table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]


def get_locations():
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM locations"
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result


def get_loc_name(location_id):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT station_name, postcode FROM locations WHERE location_id = \"{}\"".format(location_id)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result


def get_loc_id(station_name):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT location_id FROM locations WHERE station_name = \"{}\"".format(station_name)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]


def check_status(vehicle_id):
    table_name = "vehicleInfo_" + str(vehicle_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT status FROM " + table_name + " WHERE info_id = (SELECT MAX(info_id) FROM " + table_name + ")"
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]


def get_balance(cust_id):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT balance FROM customers WHERE cust_id = \"{}\"".format(cust_id)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return float(result[0][0])


def update_balance(cust_id, balance):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "UPDATE customers SET balance = \"{}\" WHERE cust_id = \"{}\"".format(round(balance, 2), cust_id)
        cursor.execute(sql)
    db.close()


def get_time(vehicle_id):
    table_name = "vehicleInfo_" + str(vehicle_id)
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT time FROM " + table_name + " WHERE info_id = (SELECT MAX(info_id) FROM " + table_name + ")"
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]


def get_type(vehicle_id):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT vehicle_type FROM vehicles WHERE vehicle_id = \"{}\"".format(vehicle_id)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]


def get_latest_vehicleInfos():
    vehicle_num = get_num("vehicles")
    results = {}
    for vehicle_id in range(1, vehicle_num + 1):
        results[vehicle_id] = get_vehicleInfo(vehicle_id)[-1]
    return results


def get_profile(cust_id):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM customers WHERE cust_id = \"{}\"".format(cust_id)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0]


def get_all_loc():
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM locations"
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result


def get_cust_id(email):
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT cust_id FROM customers WHERE email = \"{}\"".format(email)
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result[0][0]
