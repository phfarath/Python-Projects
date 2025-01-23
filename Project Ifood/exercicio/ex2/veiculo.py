class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nLigado: {'sim' if self._ligado else 'não'}'
    
    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False