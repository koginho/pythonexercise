# Objetivo: somar dois números.

def soma_numeros(a, b):
    """
        Função que soma dois números

        Recebe dois valores e realiza a operação de soma
        caso um erro de tipo ou erro de exceção ocorra uma
        mensagem aparecerá no prompt

        Args:
            a (float): primeiro valor da soma.
            b (float): segundo valor da soma.
        Returns:
            float: resultado da soma.
    """
    try:
        soma = a + b
        print(f"Resultado: {soma}")
        return soma
    except TypeError:
        print("Erro: entrada inválida")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return None

# Entrada de dados.
first_number = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo: "))

# Chamada da função.
soma_numeros(first_number, second_number)