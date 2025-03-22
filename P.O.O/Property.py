class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo "privado"
        self._idade = idade

    @property
    def idade(self):  # Getter para idade
        return self._idade

# Testando
pessoa = Pessoa("Alice", 30)
print(pessoa.idade)  # Saída: 30