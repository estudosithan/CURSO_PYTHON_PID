class DummyCarro:
    def __init__(self, modelo, placa, cor):
        self.modelo = modelo
        self.__placa = placa  # Atributo privado
        self.cor = cor
    
    def get_placa(self):
        """Método para acessar a placa do carro de forma controlada"""
        return self.__placa

class Pessoa:
    def __init__(self, nome, sobrenome, carro):
        self.nome = nome
        self.sobrenome = sobrenome
        self.carro = carro  # Recebe um objeto da classe DummyCarro
    
    def apresentar(self):
        print(f"Olá, eu sou {self.nome} {self.sobrenome} e tenho um {self.carro.modelo} {self.carro.cor}.")

# Criando um objeto da classe DummyCarro
carro_pessoa = DummyCarro("Celta", "ABC-1234", "preto")

# Criando um objeto da classe Pessoa e passando o carro como um atributo
p1 = Pessoa("Íthan", "Amaral", carro_pessoa)

# Chamando o método apresentar
p1.apresentar()

# Tentando acessar a placa diretamente (isso dará erro)
# print(p1.carro.__placa)  # AttributeError: 'DummyCarro' object has no attribute '__placa'

# Acessando a placa corretamente usando um método
print(f"A placa do carro é: {p1.carro.get_placa()}")
