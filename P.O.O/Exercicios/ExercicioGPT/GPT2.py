
#Heranças de Animais
class Animal:
    def __init__(self, raca):
        self.raca = raca

    def emitir_Som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_Som(self):
        print(f'O {self.raca} faz Au Au')

class Gato(Animal):
    def emitir_Som(self):
        print(f'O {self.raca} faz Miau Miau')

#Pegando Raças
raca_dog = input("Digite a raça do cachorro: ")
raca_cat = input("Digite a raça do gato: ")

#Executando métodos
dog = Cachorro(raca_dog)
dog.emitir_Som()
cat = Gato(raca_cat)
cat.emitir_Som()