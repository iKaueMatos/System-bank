from abc import ABC, abstractmethod

class IDatabaseConnection(ABC):
    @abstractmethod
    def connect_to_db(self):
      pass
    
    @abstractmethod
    def close_connection(self):
      pass
    
    @abstractmethod
    def execute_query(self, query, params=None):
      pass

    @abstractmethod
    def fetch_all(self, query, params=None):
      pass

    @abstractmethod
    def fetch_one(self, query, params=None):
      pass