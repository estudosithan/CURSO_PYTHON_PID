class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, grana):
        if grana > 0:
            self.saldo = self.saldo + grana
            print(f"Depósito de R$ {grana} realizado com sucesso !")
        else:
            print("Quantia insuficiente")

    def sacar(self, grana):
        if self.saldo > 0:
            self.saldo = self.saldo - grana
            print(f"Saque de R$ {grana} realizado com sucesso !")
        else:
            print("Saldo insuficiente para saque")

    def exibir_saldo(self):
        print(f"O atual saldo da conta de {self.titular} é: {self.saldo} reais")


Eu = ContaBancaria("Íthan")
Eu.exibir_saldo()
Eu.depositar(2000)
Eu.exibir_saldo()
Eu.sacar(1000)
Eu.exibir_saldo()
