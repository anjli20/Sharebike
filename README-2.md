# Project Name
The project name is **Share Bike**, it aims for providing a software system to support an electric vehicles sharing programme.

---

# Project Overview
## Vehicles
There are two types of vehicles in the system, which is **E-Bike** and **Bike**. The charging policy is a bit different for these two types.


## Status
Four statuses are provided to describe the condition of a vehicle, including **VACANT**, **RENTED**, **LOWPOWER** and **BROKEN**.

## Location
The software only supports docked bike sharing programme. An available docking position is described by two fields, which is **station name** and **postcode**.

## Customer
Customers are able to **rent** and **return** vehicles through the interface provided by the software, the system will automatically calculate the charge according to the time period of their riding, so that they can **pay** their bills later. A customer can also **report** the malfunction of vehicles, including broken parts or ran out of power. Another two features are that they have the access to the database to check their **profile** and their **travel history**.

## Operator
Operators are able to **track** all the current vehicles' location and status. They can also make changes like **charging** the battery or **repairing** bike faults. **Moving** vehicles from one place to another is also available.

## Manager
A manager has the access to the whole database and the system is able to **generate various forms of reports** to reflect the usage condition.

---

# Installation Instruction
1. Download the code, open the folder with spyder
2. Run the Initialize.py once to initialize the database and generate simulated data.
3. Run the sharebike-app-entrypoint.py to activate the user interface

![Entry](images/entry.png)

---

# Usage Guidelines
## Register
1. Click **sign up**
2. Choose register as **customer** or **operator** or **manager**
3. Enter the information and Click **sign up**
  
![Register](images/register.png)

## Login
1. Choose login as **customer** or **operator** or **manager**
2. Enter the **email** and **password** anc click **log in**

![Login](images/login.png)

## Customer
![Customer](images/customer.png)

### View Profile
Click **view profile**

![Profile](images/profile.png)

### Rent
Select **location** and **vehicle**, click **rent**

![Rent](images/rent.png)

### Return
Select **location**, click **return**

![Return](images/return.png)

### Report
Select **location**, **vehicle** and **status**, click **report**

![Report](images/report.png)

### Pay
Enter **amount**, click **pay**

![Pay](images/pay.png)

### View History
Click **history**

![History](images/history.png)

## Operator
![Operator](images/operator.png)

### Track
Click **track**

![Track](images/track.png)

### Charge
Select **vehicle**, click **charge**

![Charge](images/charge.png)

### Repair
Select **vehicle**, click **repair**

![Repair](images/repair.png)

### Move
Select **vehicle** and **location**, click **move**

![Move](images/move.png)

## Manager
![Manager](images/manager.png)

### Period Report & Full Report
- Enter the start time and the end time, formated as **%Y-%m-%d %H:%M**, click **generate report** to get the vehicle information during the span, listed as texts in the console
- Click **generate full report** to get all the vehicle information, listed as texts in the console

![Report](images/report1.png)

### Graph
Click **generate vehicle graph** to check the number of vehicles under different status

![Graph](images/graph1.png)

### Graph
Click **generate graph stations & vehicles** to check the number of vehicles in different stations

![Graph](images/graph2.png)

---

# Contributors

We'd like to thank the following contributors who have helped make this project better:

- Anjali Shishupal Gedam
- Rohit Kumar Dubey
- Sayonee Dassani
- Xuzhe Huang