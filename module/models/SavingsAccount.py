from module.models.AccountBank import AccountBank
from module.interface.IAccount import IAccount
from module.service.EmailService import EmailService

class SavingsAccount(AccountBank, IAccount):
    def __init__(self, email_service= None,
                 name: str = None,
                 lastname: str = None,
                 age: int = None,
                 numberAccount: int = None,
                 agency: int = None,
                 balance: float = None,
                 state: str = None,
                 interest_rate: float = 0.0
    ) -> None:
        super().__init__(name, lastname, age, numberAccount, agency, balance, state)
        self.__interest_rate = interest_rate
        self.email_service = email_service if email_service is not None else EmailService()

    def inicialization(self):
        messageStandard = ("Seja bem vindo! Para prosseguirmos com seu cadastro na conta poupança "
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
        if self.__interest_rate is None:
            self.__interest_rate = float(input("Digite a taxa de juros: "))
        self.email = input("Digite seu e-mail: ")

    def validate_bank_account_creation_data(self) -> str:
        base_validation = super().validate_bank_account_creation_data()
        if base_validation != "Usuário válido!":
            return base_validation
        if self.__interest_rate <= 0.0:
            return "A taxa de juros deve ser maior que zero para a conta poupança."
        return "Usuário válido!"

    def validate_creation_data_user(self) -> str:
        base_validation = super().validate_creation_data_user()
        if base_validation != "Usuário válido!":
            return base_validation
        return "Usuário válido!"

    def withdraw(self, withdraw_value: float) -> None:
        if withdraw_value > self.balance:
            raise ValueError("Saldo insuficiente.")
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

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    def set_interest_rate(self, interest_rate: float) -> None:
        if interest_rate <= 0:
            raise ValueError("A taxa de juros deve ser maior que zero.")
        self.__interest_rate = interest_rate

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
        
    def get_agency(self) -> int:
        return self.agency
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
