from modelo.cardapio.item_cardapio import ItemCardapio

# herança de classes - herdando as informações do ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # refere-se à instanciação da herança com a passagem de parametros
        ItemCardapio.__init__(self, nome, preco)
        # _ - método privado 
        self.descricao = descricao
    
    def __str__(self):
        return f"{ItemCardapio.__str__(self)} - {self.descricao}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)