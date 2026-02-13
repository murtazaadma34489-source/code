from abc import ABC, abstractmethod
import mysql.connector as connector

# ================== DATABASE CONNECTION ==================
mydb = connector.connect(
    host="localhost",
    user="root",
    password="murtaza123"
)
cursor = mydb.cursor()

# ================== CREATE DATABASE AND TABLES ==================
cursor.execute("CREATE DATABASE IF NOT EXISTS event_management_db")
cursor.execute("USE event_management_db")

# VENUE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS venue (
    venue_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
)
""")

# EVENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS event (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100),
    event_type VARCHAR(50),
    fixed_charges DOUBLE,
    service_charges DOUBLE,
    event_date VARCHAR(20),
    venue_id INT,
    FOREIGN KEY (venue_id) REFERENCES venue(venue_id)
)
""")

# WEDDING EVENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS wedding_event (
    wedding_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    guests INT,
    cost_per_guest DOUBLE,
    tax_per_guest DOUBLE
)
""")

# BIRTHDAY EVENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS birthday_event (
    birthday_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    cake_price DOUBLE,
    decoration DOUBLE
)
""")

# CONFERENCE EVENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS conference_event (
    conference_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    corporate_tax DOUBLE
)
""")

# LOGIN TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL
)
""")
mydb.commit()

# ================== VENUE CLASS ==================
class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def save(self):
        cursor.execute(
            "INSERT INTO venue (name, city) VALUES (%s,%s)",
            (self.name, self.city)
        )
        mydb.commit()
        return cursor.lastrowid

    def __str__(self):
        return f"{self.name}, {self.city}"

# ================== ABSTRACT EVENT ==================
class Event(ABC):
    def __init__(self, name, venue, date, fixed):
        self.name = name
        self.venue = venue
        self.date = date
        self.fixed_charges = fixed
        self.service_charges = fixed * 0.10

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def display(self):
        pass

# ================== WEDDING EVENT ==================
class WeddingEvent(Event):
    def __init__(self, name, venue, date, fixed, guests, cost_guest, tax_guest):
        super().__init__(name, venue, date, fixed)
        self.guests = guests
        self.cost_guest = cost_guest
        self.tax_guest = tax_guest

    def calculate_cost(self):
        guest_cost = self.guests * self.cost_guest
        tax = guest_cost * (self.tax_guest / 100)
        return self.fixed_charges + self.service_charges + guest_cost + tax

    def save(self):
        venue_id = self.venue.save()
        cursor.execute("""
            INSERT INTO event (event_name,event_type,fixed_charges,service_charges,event_date,venue_id)
            VALUES (%s,'Wedding',%s,%s,%s,%s)
        """, (self.name, self.fixed_charges, self.service_charges, self.date, venue_id))
        mydb.commit()
        eid = cursor.lastrowid
        cursor.execute("""
            INSERT INTO wedding_event (event_id, guests, cost_per_guest, tax_per_guest)
            VALUES (%s,%s,%s,%s)
        """, (eid, self.guests, self.cost_guest, self.tax_guest))
        mydb.commit()

    def display(self):
        print(f"Event Name: {self.name}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.date}")
        print(f"Fixed Charges: PKR{self.fixed_charges:.2f}")
        print(f"Service Charges: PKR{self.service_charges:.2f}")
        print(f"Number of Guests: {self.guests}")
        print(f"Cost Per Guest: PKR{self.cost_guest:.2f}")
        print(f"Service Tax Per Guest: {self.tax_guest:.2f}%")
        print(f"Total Cost: PKR{self.calculate_cost():.2f}")
        print()

# ================== BIRTHDAY EVENT ==================
class BirthdayEvent(Event):
    def __init__(self, name, venue, date, fixed, cake, decor):
        super().__init__(name, venue, date, fixed)
        self.cake_price = cake
        self.decoration = decor

    def calculate_cost(self):
        return self.fixed_charges + self.service_charges + self.cake_price + self.decoration

    def apply_discount(self):
        self.cake_price *= 0.90

    def save(self):
        venue_id = self.venue.save()
        cursor.execute("""
            INSERT INTO event (event_name,event_type,fixed_charges,service_charges,event_date,venue_id)
            VALUES (%s,'Birthday',%s,%s,%s,%s)
        """, (self.name, self.fixed_charges, self.service_charges, self.date, venue_id))
        mydb.commit()
        eid = cursor.lastrowid
        cursor.execute("""
            INSERT INTO birthday_event (event_id, cake_price, decoration)
            VALUES (%s,%s,%s)
        """, (eid, self.cake_price, self.decoration))
        mydb.commit()

    def display(self):
        print(f"Event Name: {self.name}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.date}")
        print(f"Fixed Charges: PKR{self.fixed_charges:.2f}")
        print(f"Service Charges: PKR{self.service_charges:.2f}")
        print(f"Cake Price: PKR{self.cake_price:.2f}")
        print(f"Decoration Charges: PKR{self.decoration:.2f}")
        print(f"Total Cost: PKR{self.calculate_cost():.2f}")
        print()

# ================== CONFERENCE EVENT ==================
class ConferenceEvent(Event):
    def __init__(self, name, venue, date, fixed, tax):
        super().__init__(name, venue, date, fixed)
        self.corporate_tax = tax

    def calculate_cost(self):
        return self.fixed_charges + self.service_charges + (self.fixed_charges * self.corporate_tax / 100)

    def save(self):
        venue_id = self.venue.save()
        cursor.execute("""
            INSERT INTO event (event_name,event_type,fixed_charges,service_charges,event_date,venue_id)
            VALUES (%s,'Conference',%s,%s,%s,%s)
        """, (self.name, self.fixed_charges, self.service_charges, self.date, venue_id))
        mydb.commit()
        eid = cursor.lastrowid
        cursor.execute("""
            INSERT INTO conference_event (event_id, corporate_tax)
            VALUES (%s,%s)
        """, (eid, self.corporate_tax))
        mydb.commit()

    def display(self):
        print(f"Event Name: {self.name}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.date}")
        print(f"Fixed Charges: PKR{self.fixed_charges:.2f}")
        print(f"Service Charges: PKR{self.service_charges:.2f}")
        print(f"Corporate Tax: {self.corporate_tax:.2f}%")
        print(f"Total Cost: PKR{self.calculate_cost():.2f}")
        print()

# ================== LOGIN FUNCTIONS ==================
def register_user():
    print("\n--- Register New User ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("SELECT * FROM login WHERE username=%s", (username,))
    if cursor.fetchone():
        print("❌ Username already exists!")
        return False
    
    cursor.execute("INSERT INTO login (username, password) VALUES (%s,%s)", (username, password))
    mydb.commit()
    print("✅ Registration successful!")
    return True

def login_user():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone():
        print(f"✅ Welcome {username}!")
        return True
    else:
        print("❌ Invalid username or password!")
        return False

# ================== MENU FUNCTIONS ==================
def add_event():
    print("\n1. Wedding Event\n2. Birthday Event\n3. Conference Event")
    choice = int(input("Select Event Type: "))
    ename = input("Enter Event Name: ")
    date = input("Enter Date (dd/mm/yyyy): ")
    fixed = float(input("Enter Fixed Charges: "))
    vname = input("Enter Venue Name: ")
    vcity = input("Enter Venue City: ")
    venue = Venue(vname, vcity)

    if choice == 1:
        guests = int(input("Number of Guests: "))
        cost = float(input("Cost per Guest: "))
        tax = float(input("Tax per Guest (%): "))
        event = WeddingEvent(ename, venue, date, fixed, guests, cost, tax)
    elif choice == 2:
        cake = float(input("Cake Price: "))
        decor = float(input("Decoration Charges: "))
        event = BirthdayEvent(ename, venue, date, fixed, cake, decor)
    elif choice == 3:
        corp_tax = float(input("Corporate Tax (%): "))
        event = ConferenceEvent(ename, venue, date, fixed, corp_tax)
    else:
        print("Invalid Choice")
        return

    event.save()
    print("✅ Event saved successfully")

def view_events():
    print("\n📌 All Events:")
    cursor.execute("""
        SELECT e.event_id, e.event_name, e.event_type, v.name, v.city, e.fixed_charges, e.service_charges, e.event_date
        FROM event e JOIN venue v ON e.venue_id=v.venue_id
    """)
    rows = cursor.fetchall()
    for r in rows:
        print(r)

def update_wedding_cost():
    wid = int(input("Enter Wedding ID to update: "))
    new_cost = float(input("Enter new cost per guest: "))
    cursor.execute("UPDATE wedding_event SET cost_per_guest=%s WHERE wedding_id=%s", (new_cost, wid))
    mydb.commit()
    print("✏ Wedding cost updated")

def delete_event():
    etype = input("Enter event type to delete (Wedding/Birthday/Conference): ")
    cursor.execute("DELETE FROM event WHERE event_type=%s", (etype,))
    mydb.commit()
    print("🗑 Event deleted")

# ================== LOGIN SYSTEM ==================
while True:
    print("\n--- EVENT MANAGEMENT LOGIN ---")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        if login_user():
            break
    elif choice == 2:
        register_user()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice, try again!")

# ================== MAIN MENU ==================
while True:
    print("\n--- EVENT MANAGEMENT ---")
    print("1. Add Event")
    print("2. View Events")
    print("3. Update Wedding Cost")
    print("4. Delete Event")
    print("5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_event()
    elif choice == 2:
        view_events()
    elif choice == 3:
        update_wedding_cost()
    elif choice == 4:
        delete_event()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again!")
