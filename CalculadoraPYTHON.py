def soma(a , b):
    return a + b

def subtracao(a , b):
    return a - b

def multiplicacao(a , b):
    return a * b

def divisao(a , b):
    return a / b

def exibir_menu():
    print("=== CALCULADORA ===")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("0 - SAIR")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)
        return resultado_convertido
    
    return resultado

opcoes_validas = {"1", "2", "3", "4", "0"}

resultado_atual = float(input("Digite o valor inicial: "))

while True:
    resultado_formatado = formatar_resultado(resultado_atual)
    print(f"Resultado atual: {resultado_formatado}")
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "0":
        print("Encerrando a calculadora.")
        break

    if opcao_escolhida not in opcoes_validas:       #not in -> não pertença
        print("\nOpção inválida.")
        print("Opções válidas: 1, 2, 3, 4 e 0\n ")

        continue        #não executa o restante, volta o while

    try:
        valor_operando = float(input("Digite o próximo valor do operando: "))
    except ValueError:
        print("Número inválido.")
        continue


    if opcao_escolhida == "1":
        resultado_atual = soma(resultado_atual,valor_operando)
    elif opcao_escolhida == "2":
        resultado_atual = subtracao(resultado_atual,valor_operando)
    elif opcao_escolhida == "3":
        resultado_atual = multiplicacao(resultado_atual,valor_operando)
    elif opcao_escolhida == "4":
        resultado_atual = divisao(resultado_atual,valor_operando)