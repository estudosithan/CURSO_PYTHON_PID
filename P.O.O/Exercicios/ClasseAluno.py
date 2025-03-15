import sys  # Importa a biblioteca para sair do programa


class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def atribuir(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        print(f"A média é {media}")
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = (
            self.calcular_media()
        )  # como é um método da classe, pode ser acessado com "self"

        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

    def apresenta_notas(self):
        for nota in self.notas:
            print(nota)

    def exibir_informacoes(self):
        media = self.calcular_media()
        situacao = self.verificar_situacao()
        print(f"Aluno: {self.nome}")
        print(f"Notas: {self.notas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")


print("Boas vindas ao sistema de Notas da Escola Amaral !")
nome = input("Digita o nome do aluno: ")
notas = eval(input("Digite as notas em formato de lista: "))
Aluno1 = Aluno(nome, notas)


while True:
    print("Digite o que quiser fazer: ")
    print(" 1 - Para Atribuir")
    print(" 2 - Para calcular a média")
    print(" 3 - Para apresentar Notas")
    print(" 4 - Para exibir informações gerais")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        nota = int(input("Digite a nota: "))
        if nota < 0:
            print("Nota inválida !")
        else:
            Aluno1.atribuir(nota)

    elif escolha == 2:
        Aluno1.calcular_media()

    elif escolha == 3:
        Aluno1.apresenta_notas()

    elif escolha == 4:
        Aluno1.exibir_informacoes()

    elif escolha == 0:
        sys.exit()
