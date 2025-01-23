from modelo.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        ItemCardapio.__init__(self, nome, preco)
        self._tamanho = tamanho 

    def __str__(self):
        return f"{ItemCardapio.__str__(self)} - {self._tamanho}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)