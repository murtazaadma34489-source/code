import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="murtaza123",
            database="etms_db"
        )
        
        self.cursor = self.conn.cursor()
        print("Database connected successfully.")

    def execute(self, query, params=None):
         self.cursor.execute(query, params or ())
         self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()
