import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


CAMINHO_ARQUIVO = "criando_json.json"
P1 = Pessoa("Ithan", 19)
P2 = Pessoa("Halisson", 21)
P3 = Pessoa("Emerson", 19)
P4 = Pessoa("Camille", 23)
bd = [vars(P1), vars(P2), vars(P3), vars(P4)]  # transforma os objetos em dicionarios
# cria uma lista por que é uma coleção de informações.

with open(CAMINHO_ARQUIVO, "w") as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
