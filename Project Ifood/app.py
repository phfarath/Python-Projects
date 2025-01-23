from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato
from modelo.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
sobremesa_panacota = Sobremesa('Panacota', 25.00, 'Pudim', '200g')
sobremesa_panacota.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(sobremesa_panacota)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()