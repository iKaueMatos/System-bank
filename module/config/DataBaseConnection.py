import sqlite3

class DataBaseConnection:
    def __init__(self, db_name='system_bank.db'):
        self.db_name = db_name
        self.conn = None

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to database {self.db_name}")
            return self.conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print(f"Connection to database {self.db_name} closed.")

    def execute_query(self, query, params=None):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()
                return cursor
            except sqlite3.Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No connection to database.")
            return None

    def fetch_all(self, query, params=None):
        if self.conn:
            try:
                cursor = self.execute_query(query, params)
                if cursor:
                    return cursor.fetchall()
                else:
                    return None
            except sqlite3.Error as e:
                print(f"Error fetching all rows: {e}")
                return None
        else:
            print("No connection to database.")
            return None

    def fetch_one(self, query, params=None):
        if self.conn:
            try:
                cursor = self.execute_query(query, params)
                if cursor:
                    return cursor.fetchone()
                else:
                    return None
            except sqlite3.Error as e:
                print(f"Error fetching one row: {e}")
                return None
        else:
            print("No connection to database.")
            return None
