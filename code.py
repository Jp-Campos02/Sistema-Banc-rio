class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0
        self.LIMITE_SAQUE = 500.0
        self.MAX_SAQUES_DIARIOS = 3
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor):
        if self.saques_diarios >= self.MAX_SAQUES_DIARIOS:
            print("Limite de saques diários atingido.")
        elif valor > self.LIMITE_SAQUE:
            print(f"O limite por saque é de R$ {self.LIMITE_SAQUE:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")
    
    def visualizar_extrato(self):
        print("\n=== Extrato ===")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("================")

# Exemplo de uso do sistema
banco = Banco()

while True:
    print("\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.visualizar_extrato()
    elif opcao == "4":
        print("Obrigado por usar nosso sistema bancário!")
        break
    else:
        print("Opção inválida. Tente novamente.")
