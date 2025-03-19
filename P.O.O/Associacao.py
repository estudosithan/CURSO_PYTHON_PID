class Escritor:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        print(f"{self.nome} está escrevendo...")

class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print(f"Caneta {self.marca} está sendo usada para escrever...")

class Escritorio:
    def __init__(self, escritor, caneta):
        self.escritor = escritor  # Associação
        self.caneta = caneta  # Associação

    def trabalhar(self):
        self.escritor.escrever()
        self.caneta.escrever()

escritor = Escritor("João")
caneta = Caneta("Bic")
escritorio = Escritorio(escritor, caneta)
escritorio.trabalhar()