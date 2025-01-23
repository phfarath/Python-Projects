class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome 
        self.endereco = endereco
    
    def __str__(self):
        return f'{self.nome} - {self.endereco}'