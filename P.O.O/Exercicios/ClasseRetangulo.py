class Retangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calculaArea(self):
        area = self.altura * self.base
        print(f"A área do retângulo é de {area}")

    def calculaPerimetro(self):
        permietro = 2 * (self.altura + self.base)
        print(f"O perímetro é de {permietro}")


MeuRetangulo = Retangulo(3, 7)

MeuRetangulo.calculaArea()
MeuRetangulo.calculaPerimetro()
