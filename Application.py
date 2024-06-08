import asyncio
from module.Infra.DAO.AccountDAO import AccountDAO
from module.config.DataBaseConnection import DataBaseConnection
from module.controllers.AccountController import AccountController
from module.migration.MigrationCreatedTable import MigrationCreatedTable
from module.models.CurrentAccount import CurrentAccount
from module.models.SavingsAccount import SavingsAccount
from module.service import EncryptionManagerService
from module.views.ConsoleView import ConsoleView

class AppInitializer:
    def __init__(self):
        self.account_DAO = AccountDAO
        self.console_view = ConsoleView()
        self.account_controller = AccountController()
        self.db_connection = DataBaseConnection().connect_to_db()
        self.migration_created_table = MigrationCreatedTable(self.db_connection)
        self.encryption_manager = EncryptionManagerService

    def initialize_encryption_manager(self):
        key = self.encryption_manager.get_key()
        if key is None:
            encryption_manager = EncryptionManagerService()
            self.encryption_manager.insert_key(encryption_manager.get_key())
        else:
            encryption_manager = EncryptionManagerService(key.encode())
        return encryption_manager

    def create_account(self):
        account_map = {
            'p': SavingsAccount,
            'c': CurrentAccount
        }

        account = None
        while account is None:
            account_type = input("Você gostaria de criar uma conta poupança ou corrente? (p/c): ").strip().lower()
            account_class = account_map.get(account_type)
            if account_class:
                account = account_class()
            else:
                print("Opção inválida! Por favor, escolha 'p' para poupança ou 'c' para corrente.")

        return account

    def initialize_account(self, account):
        account.initialize_data()
        validation_message = account.validate_bank_account_creation_data()

        if validation_message != "Usuário válido!":
            print(f"Erro na criação da conta bancária: {validation_message}")
            return None

        user_validation_message = account.validate_creation_data_user()
        if user_validation_message != "Usuário válido!":
            print(f"Erro na validação dos dados do usuário: {user_validation_message}")
            return None

        return account

    def confirm_email(self, account):
        email = account.get_email()

        while email:
            recipient_confirmation = input(f"Seu email de confirmação é este {email}? (s/n): ").strip().lower()
            if recipient_confirmation == 's':
                account.send_confirmation_email(email)
                break
            elif recipient_confirmation == 'n':
                email = input("Digite seu email novamente: ")
                account.set_email(email)
            else:
                print("Opção inválida! Por favor, escolha 's' ou 'n'.")
        else:
            print("O email não foi fornecido. Não é possível enviar a confirmação.")

    def process_options(self, account):
        options_map = {
            "1": self.show_balance,
            "2": self.deposit_amount,
            "3": self.withdraw_amount,
            "4": self.consult_user_exist,
            "5": self.exit
        }

        while True:
            self.console_view.display_options()
            option = self.console_view.get_option_choice()
            action = options_map.get(option, self.invalid_option)
            action(account)

    def show_balance(self, account):
        balance = self.account_controller.get_account_balance(account)
        self.console_view.display_message(f"Seu saldo atual é: {balance}")

    def deposit_amount(self, account):
        amount = float(self.console_view.get_input("Digite o valor do depósito: "))
        self.account_controller.deposit(account, amount)
        self.console_view.display_message("Depósito realizado com sucesso!")

    def withdraw_amount(self, account):
        amount = float(self.console_view.get_input("Digite o valor da retirada: "))
        try:
            self.account_controller.withdraw(account, amount)
            self.console_view.display_message("Retirada realizada com sucesso!")
        except ValueError as e:
            self.console_view.display_message(f"Erro: {e}")

    def consult_user_exist(self, account):
        account_number = account.get_number_account()
        user = self.account_DAO.consult_account(account_number)
        if user:
            print(f"Usuario encontrado: {user}")
        else:
            print("Usuário não foi encontrado no banco de dados.")

    def exit(self, account):
        self.console_view.display_message("Obrigado por utilizar nosso sistema!")
        self.db_connection.close()
        raise SystemExit

    def invalid_option(self, account):
        self.console_view.display_message("Opção inválida! Tente novamente.")

    def run(self):
        self.migration_created_table.create_tables()
        account = self.create_account()
        if account:
            account = self.initialize_account(account)
            if account:
                name = account.get_name()
                email = account.get_email()
                balance = account.get_balance_account()
                account_number = account.get_number_account()
                agency = account.get_agency()
                
                encrypted_name = self.encryption_manager.encrypt(name)
                encrypted_email = self.encryption_manager.encrypt(email)
                encrypted_balance = self.encryption_manager.encrypt(str(balance))
                encrypted_account_number = self.encryption_manager.encrypt(account_number)
                encrypted_agency = self.encryption_manager.encrypt(agency)

                self.account_DAO.insert_account(
                    name=encrypted_name,
                    email=encrypted_email,
                    balance=encrypted_balance,
                    account_number=encrypted_account_number,
                    agency=encrypted_agency
                )
                
                self.confirm_email(account)
                self.process_options(account)
