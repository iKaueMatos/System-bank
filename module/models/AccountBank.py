from module.service.EmailService import EmailService


class AccountBank:
    def __init__(self, email_service, name=None, lastname=None, age=None, numberAccount=None, agency=None, balance=None, state=None):
        self.email_service = EmailService()
        self.name = name
        self.lastname = lastname
        self.age = age
        self.numberAccount = numberAccount
        self.agency = agency
        self.balance = balance
        self.state = state

    def __validateBankAccountCreationData(self):
        if not all([self.name, self.lastname, self.age, self.numberAccount, self.agency, self.balance, self.state]):
            return "Dados incompletos para a criação da conta bancária."
        return "Usuário válido!"

    def __validateCreationDataUser(self):
        if not all([self.name, self.lastname, self.age]):
            return "Dados incompletos para a criação do usuário."
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