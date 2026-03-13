# Objetivo: criar uma função que recebe dois parametros (number, string)
# a função deve virificar e exibir esses valores.
from operator import length_hint

# Recebe os valores do usuário
minhaString = input('Digite um texto: ')
meuNumero = int(input('Digite um número inteiro: '))

def imprimir_parametros(texto, numero):
    """
    Função que imprime dois valores.

    Esta função recebe dois valores, verifica se texto = str e se numero = int
    e imprime o valor.

    Args:
        texto(string): valor atribuido pelo usuário.
        numero(int): valor atribuido pelo usuário.
    Returns:
        None: sem retorno.
    """
    if texto.replace(" ", "").isalpha():
        print(texto)
    else:
        print("texto inválido.")

    if isinstance(numero, int):
        print(numero)
    else:
        print("número inválido.")

# Chamada da função
imprimir_parametros(minhaString, meuNumero)
