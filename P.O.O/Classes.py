# PascalCase


class NomePessoas:
    def __init__(self, nome, sobrenome, carro):  # faz as atribuições
        self.apodo = (
            nome  # posso criar atributos com nome diferente do parâmetro passado
        )
        self.sobrenome = sobrenome
        self.carro = carro

    # self serve para criar um atributo da própria classse pra ela mesma

    def acelerar(self):
        print("está acelerando...")

    def freiar(self):
        print(f"O carro {self.apodo} está freiando")


p1 = NomePessoas("Íthan", "Amaral", "Celta")


p2 = NomePessoas("Gisely", "Melo", "BMW")


print(
    f"O {p1.carro} de {p1.apodo} {p1.sobrenome} "
), p1.acelerar()  # se o método estivesse dentro do print, devolveria none, por que ele já tem um print já
print("")
print(p2.apodo, p2.sobrenome)
