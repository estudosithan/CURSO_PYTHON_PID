class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print('teste de return')
        return "faz Som genérico"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da superclasse
        self.raca = raca

    def fazer_som(self):
        return super().fazer_som() #da para usar o super para reutilizar código também, maaaas é importante por depois do return se não não funciona

dog = Cachorro("Rex", "Labrador")
print(dog.nome)  # Rex
print(dog.fazer_som())  # Au au!
print(Cachorro.mro())

