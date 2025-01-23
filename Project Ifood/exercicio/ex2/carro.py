from exercicio.ex2.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        Veiculo.__init__(self, marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{Veiculo.__str__(self)}\nPortas: {self.portas}'