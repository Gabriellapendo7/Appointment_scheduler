# import sqlite3
# from sqlite3 import Error

# class Database:
#     def __init__(self, db_file):
#         try:
#             self.connection = sqlite3.connect(db_file)
#             self.cursor = self.connection.cursor()
#             print("Connected to SQLite database")
#             self.create_tables()
#         except Error as e:
#             print(f"Error: {e}")
#             self.connection = None
#             self.cursor = None

#     def create_tables(self):
#         client_table = """
#         CREATE TABLE IF NOT EXISTS clients (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT NOT NULL
#         );
#         """
#         appointment_table = """
#         CREATE TABLE IF NOT EXISTS appointments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             client_id INTEGER NOT NULL,
#             date TEXT NOT NULL,
#             time TEXT NOT NULL,
#             FOREIGN KEY (client_id) REFERENCES clients (id)
#         );
#         """
#         reminder_table = """
#         CREATE TABLE IF NOT EXISTS reminders (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             appointment_id INTEGER NOT NULL,
#             reminder_date TEXT NOT NULL,
#             reminder_message TEXT NOT NULL,
#             FOREIGN KEY (appointment_id) REFERENCES appointments (id)
#         );
#         """
#         self.execute_query(client_table)
#         self.execute_query(appointment_table)
#         self.execute_query(reminder_table)

#     def execute_query(self, query, params=None):
#         if self.connection is None or self.cursor is None:
#             print("Not connected to the database")
#             return
#         self.cursor.execute(query, params or ())
#         self.connection.commit()

#     def fetch_all(self, query, params=None):
#         if self.connection is None or self.cursor is None:
#             print("Not connected to the database")
#             return []
#         self.cursor.execute(query, params or ())
#         return self.cursor.fetchall()

#     def close(self):
#         if self.cursor:
#             self.cursor.close()
#         if self.connection:
#             self.connection.close()



# app/db/database.py

import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            conn.row_factory = sqlite3.Row  # This allows us to access columns by name
            print("Connected to SQLite database")
            return conn
        except sqlite3.Error as e:
            print(e)
            return None

    def execute(self, query, params=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor
        except sqlite3.Error as e:
            print(e)
            return None

    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
