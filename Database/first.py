import mysql.connector as connector

print("Welcome to Smart Bus Management & Tracking System")

# ================= DATABASE CONNECTION =================
mydb = connector.connect(
    host="localhost",
    user="root",
    passwd="murtaza123"
)
mycursor = mydb.cursor()

# ================= DATABASE =================
mycursor.execute("CREATE DATABASE IF NOT EXISTS SBMTS_db")
print("Database created!")

mycursor.execute("USE SBMTS_db")

# ================= TABLES =================
mycursor.execute("""
CREATE TABLE IF NOT EXISTS login(
    username VARCHAR(25),
    password VARCHAR(25)
)
""")
print("Login table created")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS bus(
    bus_id INT,
    bus_number VARCHAR(20),
    capacity INT
)
""")
print("Bus table created")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS driver(
    driver_id INT,
    name VARCHAR(50),
    contact BIGINT,
    license_no BIGINT
)
""")
print("Driver table created")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS route(
    route_id INT,
    source VARCHAR(50),
    destination VARCHAR(50)
)
""")
print("Route table created")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS schedule(
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT,
    route_id INT,
    departure_time VARCHAR(20),
    arrival_time VARCHAR(20)
)
""")
print("Schedule table created")

mydb.commit()

# ================= ADMIN DEFAULT =================
mycursor.execute("SELECT * FROM login")
if mycursor.fetchone() is None:
    mycursor.execute("INSERT INTO login VALUES ('murtaza','murtaza123')")
    mydb.commit()

# ================= MAIN MENU =================
while True:
    print("""
     1. Admin
     2. User
     3. Exit
      """)
    ch = int(input("Enter choice: "))

    # ================= ADMIN =================
    if ch == 1:
        pwd = input("Enter admin password: ")
        mycursor.execute("SELECT password FROM login")
        if pwd == mycursor.fetchone()[0]:
            print("Welcome Admin")

            while True:
                print("""
            1. Add Bus
            2. Add Driver
            3. Add Route
            4. Add Schedule
            5. View All Buses
            6. Logout
             """)
                ch = int(input("Enter choice: "))

                if ch == 1:
                    bus_id = int(input("Bus ID: "))
                    bus_no = input("Bus Number: ")
                    cap = int(input("Capacity: "))
                    mycursor.execute(
                        "INSERT INTO bus VALUES (%s,%s,%s)",
                        (bus_id, bus_no, cap)
                    )
                    mydb.commit()
                    print("Bus added successfully")

                elif ch == 2:
                    did = int(input("Driver ID: "))
                    name = input("Name: ")
                    contact = int(input("Contact: "))
                    lic = int(input("License No: "))
                    mycursor.execute(
                        "INSERT INTO driver VALUES (%s,%s,%s,%s)",
                        (did, name, contact, lic)
                    )
                    mydb.commit()
                    print("Driver added")

                elif ch == 3:
                    rid = int(input("Route ID: "))
                    src = input("Source: ")
                    dest = input("Destination: ")
                    mycursor.execute(
                        "INSERT INTO route VALUES (%s,%s,%s)",
                        (rid, src, dest)
                    )
                    mydb.commit()
                    print("Route added")

                elif ch == 4:
                    bus_id = int(input("Bus ID: "))
                    route_id = int(input("Route ID: "))
                    dep = input("Departure Time: ")
                    arr = input("Arrival Time: ")
                    mycursor.execute(
                        "INSERT INTO schedule (bus_id,route_id,departure_time,arrival_time) VALUES (%s,%s,%s,%s)",
                        (bus_id, route_id, dep, arr)
                    )
                    mydb.commit()
                    print("Schedule added")

                elif ch == 5:
                    mycursor.execute("SELECT * FROM bus")
                    print("ID | NUMBER | CAPACITY")
                    for i in mycursor:
                        print(i)

                elif ch == 6:
                    break
        else:
            print("Wrong password")

    # ================= USER =================
    elif ch == 2:
        print("""
       1. View Bus Schedule
       2. View Routes
       3. Go Back
       """)
        ch = int(input("Enter choice: "))

        if ch == 1:
            mycursor.execute("""
            SELECT schedule.schedule_id, bus.bus_number, route.source, route.destination,
            schedule.departure_time, schedule.arrival_time
            FROM schedule
            JOIN bus ON schedule.bus_id = bus.bus_id
            JOIN route ON schedule.route_id = route.route_id
            """)
            print("ID | BUS | FROM | TO | DEP | ARR")
            for i in mycursor:
                print(i)

        elif ch == 2:
            mycursor.execute("SELECT * FROM route")
            print("ID | SOURCE | DESTINATION")
            for i in mycursor:
                print(i)

        elif ch == 3:
            continue

    elif ch == 3:
        print("System Closed")
        break