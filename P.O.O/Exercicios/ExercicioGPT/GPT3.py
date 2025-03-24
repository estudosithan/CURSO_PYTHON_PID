class Mamifero:
    def amamentar(self):
        #não precisou do init por que não precisa passar nada na instância
        print("O mamífero está amamentando.")

class Aquatico:
    def nadar(self):
        #não precisou do init por que não precisa passar nada na instância
        print("O animal Aquático está nadando")

class Baleia(Mamifero, Aquatico):
    def apresentar(self):
        #não precisou do init por que não precisa passar nada na instância
        print("Hello, Eu sou uma baleia !")

baleia = Baleia()
baleia.apresentar()
baleia.amamentar()
baleia.nadar()