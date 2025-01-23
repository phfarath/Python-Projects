from exercicio.ex1.Banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        Banco.__init__(self, nome, endereco)
        self.numero = numero
    
    def __str__(self):
        return f'{Banco.__str__(self)} - {self.numero}' 
