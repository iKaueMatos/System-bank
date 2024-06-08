from module.config.DataBaseConnection import DataBaseConnection

class EncryptionDAO:
    def __init__(self, db_connection):
      self.db_connection = DataBaseConnection()
      self.conn = self.db_connection.connect_to_db()
        
    def insert_key(self, key):
        self.db_connection.execute('''INSERT INTO encryption_keys (key) VALUES (?)''', (key,))

    def get_key(self):
        cursor = self.db_connection.execute('''SELECT key FROM encryption_keys LIMIT 1''')
        row = cursor.fetchone()
        if row:
            return row[0]
        return None