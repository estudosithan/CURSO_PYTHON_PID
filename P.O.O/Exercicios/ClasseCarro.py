class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(
            f"O carro {self.marca} do modelo {self.modelo} e ano {self.ano} está acelerando..."
        )

    def desacelerar(self):
        print(f"É campeão, o bixão tá parando aqui....")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"  # Para não dar problema


MeuCarro = Carro("Honda", "Fit", "2018")
print(MeuCarro)
