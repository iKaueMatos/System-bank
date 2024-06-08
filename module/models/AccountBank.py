from module.service.EmailService import EmailService
from module.shared.validation.EmailValidation import EmailValidation


class AccountBank:
    def __init__(self, email_service,
                 email=None,
                 name=None,
                 lastname=None,
                 age=None,
                 numberAccount=None,
                 agency=None,
                 balance=None,
                 state=None,
                 overdraft_limit=None,
                 interest_rate=None
                 ):
        self.email_service = EmailService()
        self.email = email
        self.name = name
        self.lastname = lastname
        self.age = age
        self.numberAccount = numberAccount
        self.agency = agency
        self.balance = balance
        self.state = state
        self.overdraft_limit = overdraft_limit
        self.interest_rate = interest_rate

    def initialize_data(self):
        if not self.name:
            self.name = input("Digite seu nome: ")
        if not self.lastname:
            self.lastname = input("Digite seu sobrenome: ")
        if self.age is None:
            while True:
                try:
                    self.age = int(input("Digite sua idade: "))
                    if self.age <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Idade inválida. Por favor, insira um número inteiro positivo.")
        if self.numberAccount is None:
            while True:
                try:
                    self.numberAccount = input("Digite o número da conta: ")
                    if not self.numberAccount.isdigit():
                        raise ValueError
                    break
                except ValueError:
                    print("Número da conta inválido. Por favor, insira um número inteiro.")
        if self.agency is None:
            while True:
                try:
                    self.agency = input("Digite a agência: ")
                    if not self.agency.isdigit():
                        raise ValueError
                    break
                except ValueError:
                    print("Agência inválida. Por favor, insira um número inteiro.")
        if self.balance is None:
            while True:
                try:
                    self.balance = float(input("Digite o saldo inicial: "))
                    if self.balance < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Saldo inicial inválido. Por favor, insira um número não negativo.")
        if not self.state:
            self.state = input("Digite o estado: ")
        if self.overdraft_limit is None:
            while True:
                try:
                    self.overdraft_limit = float(input("Digite o limite do cheque especial: "))
                    if self.overdraft_limit < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Limite do cheque especial inválido. Por favor, insira um número não negativo.")
        if self.interest_rate is None:
            while True:
                try:
                    self.interest_rate = float(input("Digite a taxa de juros: "))
                    if self.interest_rate <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Taxa de juros inválida. Por favor, insira um número positivo.")
        while True:
            self.email = input("Digite seu e-mail: ")
            email_validator = EmailValidation()
            if email_validator.is_valid_email(email_validator, self.email):
                email_validad = self.email
                print("Email válido!")
                break
            else:
                print("Email inválido. Por favor, insira um email válido.")
                
    def validate_bank_account_creation_data(self):
        if not all([self.name, self.lastname, self.age, self.numberAccount, self.agency, self.balance, self.state]):
            return "Dados incompletos para a criação da conta bancária."
        
        if not isinstance(self.age, int) or self.age <= 0 or self.age < 18:
            return "Idade inválida. Deve ser um número inteiro positivo."
        
        if not isinstance(self.balance, (int, float)) or self.balance < 0:
            return "Saldo inválido. Deve ser um número não negativo."
        
        return "Usuário válido!"

    def validate_creation_data_user(self):
        if not all([self.name, self.lastname, self.age]):
            return "Dados incompletos para a criação do usuário."

        if not isinstance(self.age, int) or self.age <= 0 or self.age < 18:
            return "Idade inválida. Deve ser um número inteiro positivo."
        
        return "Usuário válido!"

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