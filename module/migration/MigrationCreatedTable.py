from module.config.DataBaseConnection import DataBaseConnection

class MigrationCreatedTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_tables(self):
        create_account_table_query = '''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                balance REAL NOT NULL DEFAULT 0.0,
                account_number TEXT NOT NULL UNIQUE,
                agency TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        '''
        create_encryption_keys_table_query = '''
            CREATE TABLE IF NOT EXISTS encryption_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL
            )
        '''
        self.db_connection.execute(create_account_table_query)
        self.db_connection.execute(create_encryption_keys_table_query)
        self.db_connection.commit()