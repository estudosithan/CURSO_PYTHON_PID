class Motor:
    def __init__(self):
        print("Motor criado")

    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Composição (aqui ta sendo instanciado por isso elas são necessárias uma pra outra)

    def ligar_carro(self):
        self.motor.ligar()

carro = Carro()
carro.ligar_carro()