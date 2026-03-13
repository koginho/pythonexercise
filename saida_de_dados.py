#Objetivo: Explorar diferentes maneiras diferentes de imprimir uma mesma mensagem.
from enum import nonmember

erros = []
def exibir_horas():
    tentativas = 0
    maximo = 5

    while tentativas < maximo:
        try:
            hora = int(input("Digite a hora:"))
            minutos = int(input("Digite os minutos:"))
            segundos = int(input("Digite os segundos:"))

            #f-string
            print(f"f-string: {hora}:{minutos}:{segundos}")
            #print
            print('print:' + str(hora) + ':' + str(minutos) + ':' + str(segundos))
            #format
            print('format(): {}:{}:{}'.format(hora, minutos, segundos))

            return hora, minutos, segundos
        except ValueError:
            print("Valor invalido")
            tentativas += 1
        except Exception as e:
            print("Ocorreu um erro...")
            tentativas += 1
            erros.append(e)
    print(f"Número máximo de tentativas atingido: {tentativas}")
    return None

exibir_horas()