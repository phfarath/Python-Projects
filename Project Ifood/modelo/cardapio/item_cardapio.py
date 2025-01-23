# import para classes abstratas
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self._nome} - {self._preco}"
    
    # aplicando uma classe abstrata (as classes filhas necessitarão obrigatóriamente ter este método, porém cada uma do seu jeito)
    @abstractmethod
    def aplicar_desconto(self):
        pass