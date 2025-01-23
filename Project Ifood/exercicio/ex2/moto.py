from exercicio.ex2.veiculo import Veiculo

class Moto:
    def __init__(self, marca, modelo, tipo):
        Veiculo.__init__(self, marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'{Veiculo.__str__(self)}\n{'Esportiva' if self.tipo == 1 else 'Casual'}'