class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def Apresentar(self):
        print(f'A pessoa {self.nome}, tem {self.idade} anos')


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso):
        super().__init__(nome,idade)
        self.curso = curso
    def Apresentar(self):
        print(f'A pessoa {self.nome}, tem {self.idade} anos e faz {self.curso}')

print(Pessoa("Íthan", 20).__dict__)
P1 = Aluno("Íthan",21, "Sistemas de Informação")
P1.Apresentar()
