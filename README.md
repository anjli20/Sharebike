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

### Key API functions:

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
