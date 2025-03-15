class Pessoa:
    Nome = "Íthan "

    def __init__(self, sobrenome, cpf):
        self.sobrenome = sobrenome
        self.cpf = cpf

    def exibicao(self):
        print(self.Nome + self.sobrenome + f" do cpf {self.cpf}")


P1 = Pessoa("Amaral", "107.816.296-40")
P1.exibicao()
P1.Nome = "Mário "
P1.exibicao()
del P1.Nome
P1.exibicao()
print(P1.__dict__)  # retorna também o dicionario da instancia com as chaves e valor
print(vars(P1))  # retorna o dicionário com as chaves e valores da classe
