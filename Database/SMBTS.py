import mysql.connector as connector

# ---------------- DATABASE CONNECTION ----------------
mydb = connector.connect(
    host="localhost",
    user="root",
    password="murtaza123"
)
mycursor = mydb.cursor()

print("Welcome to Smart Bus Management and Tracking System (SBMTS)")

# ---------------- DATABASE ----------------
mycursor.execute("CREATE DATABASE IF NOT EXISTS SBMTS_db")
mycursor.execute("USE SBMTS_db")

# ---------------- TABLES ----------------
mycursor.execute("""
CREATE TABLE IF NOT EXISTS login(
    username VARCHAR(25),
    password VARCHAR(25)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Vehicle(
    Vehicle_id INT,
    make VARCHAR(25),
    model INT
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Driver(
    driver_id INT,
    name VARCHAR(50),
    contact BIGINT,
    licenseNumber BIGINT,
    duty VARCHAR(50),
    assignedBus VARCHAR(50)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS BusVehicle(
    bus_id INT,
    numberPlate BIGINT,
    seatingCapacity INT,
    vehicle_id INT,
    make VARCHAR(50),
    model INT
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Stop(
    stop_id INT,
    stopName VARCHAR(100)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Route(
    route_id INT,
    stopName VARCHAR(100)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Schedule(
    schedule_id INT,
    route VARCHAR(100),
    bus INT,
    departure VARCHAR(100),
    arrival VARCHAR(100),
    status VARCHAR(50)             
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Ticket(
    ticket_id INT,
    source VARCHAR(100),
    destination VARCHAR(100),
    fare INT,
    time VARCHAR(50)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS PersonPassengers(
    passenger_id INT,
    name VARCHAR(100),
    address VARCHAR(100)
)
""")

mydb.commit()

# ---------------- INSERT ADMIN ----------------
mycursor.execute("SELECT * FROM login")
if mycursor.fetchone() is None:
    mycursor.execute("INSERT INTO login VALUES ('murtaza','murtaza123')")
    mydb.commit()

# ---------------- COMMON INSERT FUNCTION ----------------
def insert_data(query, values):
    mycursor.execute(query, values)
    mydb.commit()
    print("Record inserted successfully!\n")

# ---------------- FUNCTIONS ----------------
def add_vehicle():
    insert_data(
        "INSERT INTO Vehicle VALUES (%s,%s,%s)",
        (int(input("Vehicle ID: ")),
         input("Make: "),
         int(input("Model: ")))
    )

def add_driver():
    insert_data(
        "INSERT INTO Driver VALUES (%s,%s,%s,%s,%s,%s)",
        (int(input("Driver ID: ")),
         input("Name: "),
         int(input("Contact: ")),
         int(input("License No: ")),
         input("Duty: "),
         input("Assigned Bus: "))
    )

def add_bus():
    insert_data(
        "INSERT INTO BusVehicle VALUES (%s,%s,%s,%s,%s,%s)",
        (int(input("Bus ID: ")),
         int(input("Number Plate: ")),
         int(input("Seating Capacity: ")),
         int(input("Vehicle ID: ")),
         input("Make: "),
         int(input("Model: ")))
    )

def add_stop():
    insert_data(
        "INSERT INTO Stop VALUES (%s,%s)",
        (int(input("Stop ID: ")),
         input("Stop Name: "))
    )

def add_route():
    insert_data(
        "INSERT INTO Route VALUES (%s,%s)",
        (int(input("Route ID: ")),
         input("Stop Name: "))
    )

def add_schedule():
    insert_data(
        "INSERT INTO Schedule VALUES (%s,%s,%s,%s,%s,%s)",
        (int(input("Schedule ID: ")),
         input("Route: "),
         int(input("Bus ID: ")),
         input("Departure: "),
         input("Arrival: "),
         input("Status: "))
    )

def add_ticket():
    insert_data(
        "INSERT INTO Ticket VALUES (%s,%s,%s,%s,%s)",
        (int(input("Ticket ID: ")),
         input("Source: "),
         input("Destination: "),
         int(input("Fare: ")),
         input("Time: "))
    )

def add_passenger():
    insert_data(
        "INSERT INTO PersonPassengers VALUES (%s,%s,%s)",
        (int(input("Passenger ID: ")),
         input("Name: "),
         input("Address: "))
    )

# ---------------- LOGIN ----------------
password = input("Enter Admin Password: ")
mycursor.execute("SELECT password FROM login")
db_pass = mycursor.fetchone()[0]

if password != db_pass:
    print("Wrong Password!")
    exit()

print("Admin Login Successful!\n")

# ---------------- MAIN MENU ----------------
while True:
    print("""
1. Add Vehicle
2. Add Driver
3. Add Bus
4. Add Stop
5. Add Route
6. Add Schedule
7. Add Ticket
8. Add Passenger
9. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_vehicle()
    elif choice == 2:
        add_driver()
    elif choice == 3:
        add_bus()
    elif choice == 4:
        add_stop()
    elif choice == 5:
        add_route()
    elif choice == 6:
        add_schedule()
    elif choice == 7:
        add_ticket()
    elif choice == 8:
        add_passenger()
    elif choice == 9:
        print("System Closed")
        break
    else:
        print("Invalid Choice!")
