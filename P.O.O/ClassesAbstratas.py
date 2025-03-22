from abc import ABC, abstractmethod

# Criando uma classe abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):  # Método abstrato (sem implementação)
        pass