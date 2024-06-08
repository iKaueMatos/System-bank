from module.models.AccountBank import AccountBank
from module.interface.IAccount import IAccount
from module.service.EmailService import EmailService

class CurrentAccount(AccountBank, IAccount):
    def __init__(self, email_service= None,
                 name: str = None,
                 lastname: str = None,
                 age: int = None,
                 numberAccount: int = None,
                 agency: int = None,
                 balance: float = None,
                 state: str = None,
                 overdraft_limit: float = None
    ) -> None:
        super().__init__(name, lastname, age, numberAccount, agency, balance, state)
        self.email_service = email_service if email_service is not None else EmailService()
        self.__overdraft_limit = overdraft_limit

    def inicialization(self):
        messageStandard = ("Seja bem vindo! Para prosseguirmos com seu cadastro na conta corrente "
                           "é necessário preenchermos algumas informações.")

        print(messageStandard)

        if not self.name:
            self.name = input("Digite seu nome: ")
        if not self.lastname:
            self.lastname = input("Digite seu sobrenome: ")
        if self.age is None:
            self.age = int(input("Digite sua idade: "))
        if self.numberAccount is None:
            self.numberAccount = int(input("Digite o número da conta: "))
        if self.agency is None:
            self.agency = int(input("Digite a agência: "))
        if self.balance is None:
            self.balance = float(input("Digite o saldo inicial: "))
        if not self.state:
            self.state = input("Digite o estado: ")
        if self.__overdraft_limit is None:
            self.__overdraft_limit = float(input("Digite o limite do cheque especial: "))
        self.email = input("Digite seu e-mail: ")

    def validate_bank_account_creation_data(self) -> str:
        base_validation = super().validate_bank_account_creation_data()
        if base_validation != "Usuário válido!":
            return base_validation
        if self.__overdraft_limit < 0:
            return "O limite do cheque especial deve ser zero ou positivo."
        return "Usuário válido!"

    def validate_creation_data_user(self) -> str:
        base_validation = super().validate_creation_data_user()
        if base_validation != "Usuário válido!":
            return base_validation
        return "Usuário válido!"

    def withdraw(self, withdraw_value: float) -> None:
        if withdraw_value > self.balance + self.__overdraft_limit:
            raise ValueError("Saldo insuficiente, mesmo considerando o cheque especial.")
        self.balance -= withdraw_value

    def send_confirmation_email(self, recipient_email):
        subject = 'Confirmação de Criação de Conta'
        content = f"""\
          Olá {self.name} {self.lastname},

          Sua conta foi criada com sucesso.

          Detalhes da conta:
          Nome: {self.name}
          Sobrenome: {self.lastname}
          Idade: {self.age}
          Número da Conta: {self.numberAccount}
          Agência: {self.agency}
          Saldo: {self.balance}
          Estado: {self.state}

          Obrigado por escolher nosso banco!
          """
        self.email_service.send_email(recipient_email, subject, content)

    def get_email(self) -> str:
        return self.email

    def get_overdraft_limit(self) -> float:
        return self.__overdraft_limit

    def set_overdraft_limit(self, overdraft_limit: float) -> None:
        if overdraft_limit < 0:
            raise ValueError("O limite do cheque especial deve ser zero ou positivo.")
        self.__overdraft_limit = overdraft_limit

    def get_value(self) -> float:
        return self.balance

    def set_balance_account(self, value: float) -> None:
        self.balance = value

    def get_balance_account(self) -> float:
        return self.balance

    def set_deposit(self, deposit_value: float) -> None:
        self.balance += deposit_value

    def get_deposit(self) -> float:
        return self.balance
    
    def set_number_account(self, number_account) -> None:
        self.numberAccount = number_account

    def get_number_account(self) -> int:
        return self.numberAccount
       
    def set_agency(self, agency):
        self.agency = agency
        
    def get_agency(self) -> str:
        return self.agency
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
