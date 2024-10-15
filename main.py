# Classe base Conta
class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero  # Número da conta
        self.titular = titular  # Nome do titular da conta
        self.saldo = saldo  # Saldo inicial, padrão é 0

    def depositar(self, valor):
        """Deposita um valor na conta, se o valor for positivo."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta, se houver saldo suficiente."""
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual: R${self.saldo}")

    def resumo(self):
        """Resumo da conta, será sobrescrito nas subclasses."""
        print(f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo}")


# Classe ContaCorrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial=1000, taxa_manutencao=15):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial
        self.taxa_manutencao = taxa_manutencao

    def sacar(self, valor):
        """Saque considerando o limite de cheque especial."""
        if valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo e limite de cheque especial insuficientes para realizar o saque.")

    def cobrar_taxa_manutencao(self):
        """Cobra a taxa de manutenção mensal."""
        self.saldo -= self.taxa_manutencao
        print(f"Taxa de manutenção de R${self.taxa_manutencao} cobrada. Saldo atual: R${self.saldo}")

    def resumo(self):
        """Exibe o resumo da conta corrente."""
        print(f"Tipo de Conta: Corrente | Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo}")


# Classe ContaPoupanca que herda de Conta
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.02):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        """Aplica a taxa de juros sobre o saldo."""
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros} aplicados. Novo saldo: R${self.saldo}")

    def resumo(self):
        """Exibe o resumo da conta poupança."""
        print(f"Tipo de Conta: Poupança | Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo}")


# Testando o sistema com as classes ContaCorrente e ContaPoupanca
if __name__ == "__main__":
    # Criando uma conta corrente
    conta_corrente = ContaCorrente("12345", "João", saldo=500)
    
    # Operações com a conta corrente
    conta_corrente.depositar(300)     # Depósito de R$300
    conta_corrente.sacar(700)         # Saque de R$700
    conta_corrente.cobrar_taxa_manutencao()  # Aplicar taxa de manutenção
    conta_corrente.resumo()           # Exibir resumo da conta corrente

    print("\n")

    # Criando uma conta poupança
    conta_poupanca = ContaPoupanca("54321", "Maria", saldo=1000)
    
    # Operações com a conta poupança
    conta_poupanca.depositar(500)     # Depósito de R$500
    conta_poupanca.aplicar_juros()    # Aplicar juros
    conta_poupanca.sacar(200)         # Saque de R$200
    conta_poupanca.resumo()           # Exibir resumo da conta poupança
