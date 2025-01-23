from modelo.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        ItemCardapio.__init__(self, nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return f'{ItemCardapio.__str__(self)} - {self._tipo} - {self._tamanho}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.1)