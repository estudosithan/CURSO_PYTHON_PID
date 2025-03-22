from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):
        pass

    def dormir(self):  # Método concreto (já implementado)
        return f"{self.nome} está dormindo..."