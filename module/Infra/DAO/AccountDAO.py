from module.Infra.repository.ICrudRepository import ICrudRepository
from module.config.DataBaseConnection import DataBaseConnection

class AccountDAO(ICrudRepository):
    def __init__(self, db_connection):
        self.db_connection = DataBaseConnection()
        self.conn = self.db_connection.connect_to_db()

    def insert_account(self, name, email, balance, account_number, agency):
        insert_query = '''
            INSERT INTO accounts (name, email, balance, account_number, agency)
            VALUES (?, ?, ?, ?, ?)
        '''
        try:
            cursor = self.db_connection.execute_query(insert_query, (name, email, balance, account_number, agency))
            if cursor:
                print(f"Account for {name} inserted successfully.")
            else:
                print("Error inserting account.")
        except Exception as e:
            print(f"Error inserting account: {e}")

    def query_accounts(self):
        select_query = 'SELECT * FROM accounts'
        rows = self.db_connection.fetch_all(select_query)
        if rows:
            for row in rows:
                print(row)
        else:
            print("Error querying accounts.")

    def consult_account(self, account_number):
        select_query = 'SELECT * FROM accounts WHERE account_number = ?'
        cursor = self.db_connection.execute_query(select_query, (account_number,))
        if cursor:
            row = cursor.fetchone()
            return row
        else:
            return None

