from exercicio.ex2.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        Veiculo.__init__(self, marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{Veiculo.__str__(self)}\nPortas: {self.portas}'
    
    def ligar(self):
        if not self._ligado:
            print('Tentando ligar o Carro')
            self._ligado = True
        else:
            print('O carro já está ligado!')

    def desligar(self):
        if self._ligado:
            print('Desligando o carro...')
            self._ligado = False
        else:
            print('O carro não está ligado!')