
class ConsoleView:
    def get_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)
    
    def display_options(self):
        print("\nEscolha uma opção:")
        print("1. Ver saldo")
        print("2. Fazer depósito")
        print("3. Fazer retirada")
        print("4. Sair")

    def get_option_choice(self):
        return input("Opção: ").strip()