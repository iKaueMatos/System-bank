from abc import ABC, abstractmethod

class ICrudRepository(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_table(self):
       pass

    @abstractmethod
    def insert_account(self, name, email, balance, account_number, agency):
       pass

    @abstractmethod
    def query_accounts(self):
        pass