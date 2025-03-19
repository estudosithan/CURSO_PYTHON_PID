class Pessoa:
    Nome = "Íthan "

    def __init__(self, sobrenome, cpf):
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    @classmethod
    def exibicao(cls, pessoa):
        if hasattr(cls, "Nome"):  # Verifica se Nome existe na classe
            print(cls.Nome + pessoa.sobrenome + f" do CPF {pessoa.cpf}")
        else:
            print(pessoa.sobrenome + f" do CPF {pessoa.cpf}")


P1 = Pessoa("Amaral", "107.816.296-40")
P1.exibicao(P1)
Pessoa.Nome = "Mário "
P1.exibicao(P1)
del Pessoa.Nome
P1.exibicao(P1)
print(P1.__dict__)  # retorna também o dicionario da instancia com as chaves e valor
print(vars(P1))  # retorna o dicionário com as chaves e valores da classe
