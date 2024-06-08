import asyncio
from module.controllers.AccountController import AccountController
from module.models.CurrentAccount import CurrentAccount
from module.models.SavingsAccount import SavingsAccount
from module.views.ConsoleView import ConsoleView

class AppInitializer:
    def __init__(self):
        self.console_view = ConsoleView()
        self.account_controller = AccountController()

    def create_account(self):
        account = None
        while account is None:
            account_type = input("Você gostaria de criar uma conta poupança ou corrente? (p/c): ").strip().lower()
            if account_type == 'p':
                account = SavingsAccount()
            elif account_type == 'c':
                account = CurrentAccount()
            else:
                print("Opção inválida! Por favor, escolha 'p' para poupança ou 'c' para corrente.")
        return account

    def initialize_account(self, account):
        account.inicialization()
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

        while True:
            if email is not None:
                recipient_confirmation = input(f"Seu email de confirmação é este {email}? (s/n): ")
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
                break

    def run(self):
        account = self.create_account()
        if account:
            account = self.initialize_account(account)
            if account:
                self.confirm_email(account)
                self.process_options(account)

    def process_options(self, account):
        while True:
            self.console_view.display_options()
            option = self.console_view.get_option_choice()

            if option == "1":
                balance = self.account_controller.get_account_balance(account)
                self.console_view.display_message(f"Seu saldo atual é: {balance}")
            elif option == "2":
                amount = float(self.console_view.get_input("Digite o valor do depósito: "))
                self.account_controller.deposit(account, amount)
                self.console_view.display_message("Depósito realizado com sucesso!")
            elif option == "3":
                amount = float(self.console_view.get_input("Digite o valor da retirada: "))
                try:
                    self.account_controller.withdraw(account, amount)
                    self.console_view.display_message("Retirada realizada com sucesso!")
                except ValueError as e:
                    self.console_view.display_message(f"Erro: {e}")
            elif option == "4":
                self.console_view.display_message("Obrigado por utilizar nosso sistema!")
                break
            else:
                self.console_view.display_message("Opção inválida! Tente novamente.")
