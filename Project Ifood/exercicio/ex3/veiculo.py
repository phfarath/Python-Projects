from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nLigado: {'sim' if self._ligado else 'não'}'
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass