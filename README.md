# ShareBike — Electric Vehicle Sharing System

A Python-based software system to support a docked electric vehicle sharing programme.
The system provides a full GUI with three distinct user roles: Customer, Operator, and Manager,
each with their own set of features for managing and interacting with the shared vehicle fleet.

## Project Overview

### Vehicles

Two types of vehicles are supported, each with a different charging policy:

- Bike
- E-Bike

### Vehicle Status

Each vehicle is tracked under one of four statuses at all times:

- VACANT — available for rent
- RENTED — currently in use
- LOWPOWER — battery needs charging
- BROKEN — requires repair

### Location

The system supports a docked bike sharing model. Each docking station is identified by:

- Station Name
- Postcode

## User Roles

### Customer

- Rent a vehicle from a docking station
- Return a vehicle to a docking station
- Report a vehicle as broken or low power
- Pay outstanding charges
- View profile
- View travel history

### Operator

- Track all vehicles — current location and status
- Charge low-power vehicles
- Repair broken vehicles
- Move vehicles between stations

### Manager

- Generate a report for a specific time period
- Generate a full report of all vehicle activity
- View a graph of vehicles by status
- View a graph of vehicles by station


## Installation

1. Clone or download the repository:

```bash
git clone https://github.com/anjli20/Sharebike.git
cd Sharebike
```

2. Open the folder in Spyder (or any Python IDE).

3. Run Initialize.py once to set up the local database and insert simulated test data:

```bash
python Initialize.py
```

4. Run the entry point to launch the GUI:

```bash
python sharebike-app-entrypoint.py
```

## Usage Guide

### Register

1. Click Sign Up on the entry screen
2. Choose your role: Customer, Operator, or Manager
3. Fill in your details and click Sign Up

### Login

1. Choose your role: Customer, Operator, or Manager
2. Enter your email and password
3. Click Log In

### Customer Features

Rent - Select a location and vehicle, then click Rent.
Return - Select a return location and click Return.
Report - Select a location, vehicle, and fault status, then click Report.
Pay - Enter the amount and click Pay.
View Profile - Click View Profile to see your account details.
View History - Click History to see all your past trips, including start/end stations, time, and charge.

### Operator Features

#### Track
Click Track to view the current location and status of all vehicles.

#### Charge
Select a low-power vehicle and click Charge.

#### Repair
Select a broken vehicle and click Repair.

#### Move
Select a vehicle and a target location, then click Move.

### Manager Features

#### Period Report
Enter a start and end time in the format %Y-%m-%d %H:%M and click Generate Report.
Vehicle activity during that period is displayed in the console.

#### Full Report
Click Generate Full Report to view all vehicle activity across all time.

#### Vehicle Status Graph
Click Generate Vehicle Graph to see a breakdown of vehicles by status.

#### Stations and Vehicles Graph
Click Generate Graph Stations & Vehicles to see how many vehicles are at each station.


## File Structure

```
Sharebike/
|
|-- Initialize.py                      # Database setup and test data generation
|-- sharebike-app-entrypoint.py        # Main GUI entry point
|-- general.py                         # Register and login logic for all user types
|-- customer.py                        # Customer-facing operations
|-- employee.py                        # Operator-facing operations
|-- manager.py                         # Manager-facing reporting operations
|-- enum_values.py                     # Enum definitions for vehicle status and user type
|-- dbFun.py                           # Core database functions
|-- sharebike_customer.py              # Customer dashboard UI
|-- sharebike_customer_rent.py         # Rent UI
|-- sharebike_customer_return.py       # Return UI
|-- sharebike_customer_report.py       # Report UI
|-- sharebike_customer_pay.py          # Payment UI
|-- sharebike_customer_history.py      # History UI
|-- sharebike_customer_profile.py      # Profile UI
|-- sharebike_customer_login.py        # Customer login UI
|-- sharebike_operator.py              # Operator dashboard UI
|-- sharebike_operator_track.py        # Track UI
|-- sharebike_operator_charge.py       # Charge UI
|-- sharebike_operator_repair.py       # Repair UI
|-- sharebike_operator_move.py         # Move UI
|-- sharebike_operator_login.py        # Operator login UI
|-- sharebike_manager_login.py         # Manager login UI
|-- sharebike_manager_generatereport.py # Report generation UI
|-- sharebike_register.py              # Registration UI
|-- README.md
```

## Developer Notes

When registering or signing in, use:
```python
enum_values.UserType.USERTYPE.value
```

When changing vehicle status, use:
```python
enum_values.Status.STATUS.value
```

Key API functions:

| Function | Description |
|---|---|
| rent(vehicle_id, time, location_id, cust_id) | Returns True on success |
| returnBike(vehicle_id, time, location_id, cust_id) | Returns True on success |
| report(vehicle_id, time, status, location_id) | Updates vehicle status |
| history(cust_id) | Returns list of all trips for a customer |
| track() | Returns latest status of all vehicles |
| track_charge() | Returns all low-power vehicles |
| track_repair() | Returns all broken vehicles |
| charge(vehicle_id, time, location_id) | Returns True on success |
| repair(vehicle_id, time, location_id) | Returns True on success |
| move(vehicle_id, time, location_id) | Moves vehicle to location |
| report_single(vehicle_id) | Returns full history of one vehicle |
| report_all() | Returns full history of all vehicles |
| report_period(start_time, end_time) | Returns vehicle history for a time period |
