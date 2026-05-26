#Utilizar biblioteca Math + CalculadoraPYHTON (PYTHON_NA_PRATICA- repositorio)

from math import sqrt, log2     #importando somente raiz quadrada e logaritmo na base 2.

def soma(a , b):
    return a + b

def subtracao(a , b):
    return a - b

def multiplicacao(a , b):
    return a * b

def divisao(a , b):
    return a / b

def raiz_quadrada(a):
    return sqrt(a)

def logaritmo(a):
    return log2(a)

def exibir_menu():
    print("=== CALCULADORA ===")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - RAIZ QUADRADA (DO RESULTADO ATUAL)")
    print("6 - LOGARITMO NA BASE 2 (DO RESULTADO ATUAL)")
    print("0 - SAIR")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)
        return resultado_convertido
    
    return resultado

def main():
    opcoes_validas = {"1", "2", "3", "4", "5", "6", "0"}

    try:
        resultado_atual = float(input("Digite o valor inicial: "))
    except ValueError:
        print("Valor inicial invalido.")
        return

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
            print("Opções válidas: 1, 2, 3, 4, 5, 6 e 0\n ")

            continue        #não executa o restante, volta o while

        if opcao_escolhida in {"1", "2", "3", "4"}:
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
            try:
                resultado_atual = divisao(resultado_atual,valor_operando)
            except ZeroDivisionError:
                print("Não se pode dividir por zero.")
        elif opcao_escolhida == "5":
            try:
                resultado_atual = raiz_quadrada(resultado_atual)
            except ValueError:
                print("Não é possível calcular raiz quadrada de número negativo.")
        elif opcao_escolhida == "6":
            try:
                resultado_atual = logaritmo(resultado_atual)
            except ValueError:
                print("Logaritmo só é definido para número positivo e diferente de zero.")



main()