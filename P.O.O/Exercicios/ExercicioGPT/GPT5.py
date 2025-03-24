

class Funcionarios:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def exibir_dados(self):
        print(f"O funcionario {self.nome}, recebe {self.salario}")

class Gerente(Funcionarios):
    def __init__(self,nome,salario,bonus):
        super().__init__(nome,salario)
        self.bonus = bonus
    def exibir_dados(self):
        print(f"O gerente {self.nome}, recebe {self.salario + self.bonus}")

P1 = Funcionarios("Íthan", 20.000)
P2 = Gerente("Mário", 40.000, 20.000)

P1.exibir_dados()
P2.exibir_dados()
help(Funcionarios)