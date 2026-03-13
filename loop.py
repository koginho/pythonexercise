#Objetivo: fazer uso de estruturas de repetição e instruções de controle de fluxo

# Estrutura de repetição for:
#definindo uma sequência de nomes:
names = ["João", "Maria", "Pedro", "Junin"]

#utilizando 'continue' para pular um valor
for x in names:
    if x == "Pedro":
        continue
    else:
        print(x)

#utilizando 'break' exibir somento o nome desejado (algo como uma busca linear)
for x in names:
    if x == "Maria":
        print(x)
        break

# estrutura de repetição while:

# Simulação de um menu
option = {
    1: 'placeholder',
    2: 'placeholder',
    3: 'placeholder',
    0: 'Sair.'
}

while True:
    #para impressão das opções.
    for x in option:
        print(x, option[x])
    try:
        user_opt = int(input("Digite uma opção: "))

        match user_opt:
            case 1:
                print("Opção selecionada: 1")
            case 2:
                print("Opção selecionada: 2")
            case 3:
                print("Opção selecionada: 3")
            case 0:
                print("Saindo do programa.")
                break

    #tratamento de exceções
    except ValueError:
        print("Número invalido")
    except Exception as e:
        print(f"Erro inesperado: {e}")