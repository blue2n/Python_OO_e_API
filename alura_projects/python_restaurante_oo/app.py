from oo.restaurante import Restaurante
from oo.cardapio.bebidas import Bebidas
from oo.cardapio.prato import Prato


restaurante_casa = Restaurante('Casa', 'Caseiro')
bebida_suco = Bebidas('Suco de Goiaba', 7.0, 'grande')
bebida_suco.aplicar_desconto()
prato_escondido = Prato('Escondidinho de carne seca', 25.50, 'o escondidinho mais escondido sa cidade')
prato_escondido.aplicar_desconto()
restaurante_casa.adicionar_no_cardapio(bebida_suco)
restaurante_casa.adicionar_no_cardapio(prato_escondido)

def main():
    restaurante_casa.mostrar_cardapio

if __name__ == '__main__':
    main()
