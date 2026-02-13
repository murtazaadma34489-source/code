import sqlite3

# ================= DATABASE SETUP =================
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    discount_rate REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    discount_rate REAL,
    season TEXT,
    seasonal_discount REAL,
    tax_rate REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    discount_rate REAL,
    author TEXT
)
""")

# ================= CLASSES =================
class Product:
    def __init__(self, name, price, discount_rate):
        self._name = name
        self._price = price
        self._discount_rate = discount_rate

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        if value < 0:
            raise ValueError("Discount cannot be negative!")
        self._discount_rate = value

    def calculate_discounted_price(self):
        return self.price * (1 - self.discount_rate/100)

    def save_to_db(self):
        cursor.execute("INSERT INTO Product (name, price, discount_rate) VALUES (?, ?, ?)",
                       (self.name, self.price, self.discount_rate))
        conn.commit()

class Clothes(Product):
    def __init__(self, name, price, discount_rate, season, seasonal_discount, tax_rate):
        super().__init__(name, price, discount_rate)
        self.season = season
        self.seasonal_discount = seasonal_discount
        self.tax_rate = tax_rate

    def calculate_discounted_price(self):
        base_price = super().calculate_discounted_price()
        seasonal_price = base_price * (1 - self.seasonal_discount/100)
        final_price = seasonal_price * (1 + self.tax_rate/100)
        return final_price

    def save_to_db(self):
        cursor.execute("""INSERT INTO Clothes (name, price, discount_rate, season, seasonal_discount, tax_rate)
                          VALUES (?, ?, ?, ?, ?, ?)""",
                       (self.name, self.price, self.discount_rate, self.season, self.seasonal_discount, self.tax_rate))
        conn.commit()

class Book(Product):
    def __init__(self, name, price, discount_rate, author):
        super().__init__(name, price, discount_rate)
        self.author = author

    def save_to_db(self):
        cursor.execute("INSERT INTO Book (name, price, discount_rate, author) VALUES (?, ?, ?, ?)",
                       (self.name, self.price, self.discount_rate, self.author))
        conn.commit()

# ================= TEST CODE =================
try:
    p1 = Product("Laptop", 1000, 10)
    c1 = Clothes("Jacket", 200, 5, "Winter", 10, 5)
    b1 = Book("Python Programming", 50, 15, "John Doe")

    print("Product discounted price:", p1.calculate_discounted_price())
    print("Clothes discounted price:", c1.calculate_discounted_price())
    print("Book discounted price:", b1.calculate_discounted_price())

    # Save to DB
    p1.save_to_db()
    c1.save_to_db()
    b1.save_to_db()

    # Save output to file
    with open("inventory_output.txt", "w") as f:
        f.write(f"Product: {p1.name}, Discounted Price: {p1.calculate_discounted_price()}\n")
        f.write(f"Clothes: {c1.name}, Discounted Price: {c1.calculate_discounted_price()}\n")
        f.write(f"Book: {b1.name}, Discounted Price: {b1.calculate_discounted_price()}\n")

except Exception as e:
    print("Error:", e)
