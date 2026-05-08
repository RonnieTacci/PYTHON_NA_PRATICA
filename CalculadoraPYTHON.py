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
    print("1 - SUBTRAÇÃO")
    print("1 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("0 - SAIR")

valor_inicial = float(input("Digite o valor inicial: "))

while True:
    print(f"Resultado atual: {valor_inicial}")
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "0":
        print("Encerrando a calculadora.")
        break