
from module.models.CurrentAccount import CurrentAccount
from module.models.SavingsAccount import SavingsAccount
from module.service.EmailService import EmailService

class AccountController:
   def __init__(self, email_service = EmailService()):
        self.email_service = email_service

   def create_account(self, account_type):
        if account_type == 'p':
            return SavingsAccount(self.email_service)
        elif account_type == 'c':
            return CurrentAccount()
        else:
            raise ValueError("Tipo de conta inválido.")

   def send_confirmation_email(self, account, recipient_email):
        account.send_confirmation_email(recipient_email)

   def get_account_balance(self, account):
        return account.get_balance_account()

   def deposit(self, account, amount):
        account.deposit(amount)

   def withdraw(self, account, amount):
        account.withdraw(amount)