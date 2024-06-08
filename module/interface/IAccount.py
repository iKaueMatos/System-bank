from abc import ABC, abstractmethod

class IAccount(ABC):
    @abstractmethod
    def get_value(self) -> float:
        pass

    @abstractmethod
    def set_balance_account(self, value: float) -> None:
        pass

    @abstractmethod
    def get_balance_account(self) -> float:
        pass

    @abstractmethod
    def set_deposit(self, deposit_value: float) -> None:
        pass

    @abstractmethod
    def get_deposit(self) -> float:
        pass
