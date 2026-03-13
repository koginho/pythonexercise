#Objetivo: simular uma loja de itens para um jogo.
# O código deve exibir os itens para o usuário, que por sua vez
#poderá escolher qual item e a quantidade que deseja comprar.
# O código deve retornar o valor da compra feita pelo usuário.

#definindo os preços dos itens:
potion_price = 1.50
light_armor = 10
rusted_sword = 5.55
icredible_gigantesco_sword = 1_000_000

def item_buy(quantity: int, price: float):
    """
    Calcula o valor total de uma compra e exibe o resultado.

    Args:
        quantity (int/float): A quantidade de itens comprados.
        price (float): O preço unitário do item.
    Returns:
        float: O preço final calculado (quantidade * preço).
    """
    final_price = quantity * price
    print(f"O preço de {quantity} são {final_price} moedinhas.")
    return final_price

def market():
    """
    Essa função age como um menu interativo, permitindo a seleção e compra de itens.

    Começa com a exibição dos itens disponíveis, solicita ao usuário
    a escolha de um item, a escolha do usuário é enviada como parâmetro
    para a função "item_buy" que calcula o valor a ser pago.
    Possui um sistema de máximo de tentativas para entradas inválidas.

    Raises:
        ValueError: Caso o usuário digite algo além de números.
        Exception: Para erros inesperados.
    Note:
        Essa função faz uso de variáveis externas de preço e da função externa "item_buy".
    """

    #Exibição do menu.
    print("Itens disponíveis: ")
    print(f"1 - Potion - Preço: {potion_price}")
    print(f"2 - Light Armor - Preço: {light_armor}")
    print(f"3 - Rusted Sword - Preço: {rusted_sword}")
    print(f"4 - Icredible Gigantesco Sword - Preço: {icredible_gigantesco_sword}")
    print("Caso queira sair da loja digite: 0")

    #Variáveis de controle.
    tentativa = 0
    maximo = 5

    #Loop principal do menu
    while tentativa < maximo:
        try:
            user_item = int(input("Qual item deseja comprar? "))

            if user_item == 0:
                break

            match user_item:
                case 1:
                    user_q_potion = int(input("Quantas poções deseja? "))
                    item_buy(user_q_potion, potion_price)
                case 2:
                    user_q_lightarmor = int(input("Quantas light armor deseja? "))
                    item_buy(user_q_lightarmor, light_armor)
                case 3:
                    user_q_rusted = int(input("Quantas rusted sword deseja? "))
                    item_buy(user_q_rusted, rusted_sword)
                case 4:
                    user_q_giga_sword = int(input("Quantas INCREDIBLE GIGANTESCO SWORD deseja? "))
                    item_buy(user_q_giga_sword, icredible_gigantesco_sword)
                case _:
                    print("Parece que esse não é um item válido :(")

        except ValueError:
            print("Parece que esse não é um item válido :(")
            tentativa += 1
            print(f"Tentativas: {tentativa}:{maximo}")

        except Exception as e:
            print(f"Erro inesperado: {e}")
            tentativa += 1

    if tentativa == maximo:
        print("Suas tentativas acabaram...")

market()