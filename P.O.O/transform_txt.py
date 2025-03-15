

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
CAMINHO_ARQUIVO = 'criando_json.json'
P1 = Pessoa("Íthan", 19)
P2 = Pessoa("Hálisson", 21)
P3 = Pessoa("Emerson", 19)
bd = [vars(P1), vars(P2), vars(P3)] #transforma os objetos em dicionarios
#cria uma lista por que é uma coleção de informações

CAMINHO_ARQUIVO = 'dados.txt'

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    for pessoa in bd:
        arquivo.write(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}\n")

print("Arquivo TXT criado!")