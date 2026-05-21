carros = []

def encontar_carro(placa):
    carro_encontrado = None

    for carro in carros:
        if carro["placa"] == placa:
            carro_encontrado = carro
            break

    return carro_encontrado

def cadastras_carro():
    placa = input("Digite a placa: ")
    cor = input("Digite a cor: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))

    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "ano": ano
    }

    carros.append(carro)
    print("\nCarro cadastrado com êxito.")

def listar_carros():
    print("\n--------------------- LISTA DE CARROS ---------------------")

    for carro in carros:
        print(f"Placa: {carro["placa"]} | Cor: {carro["cor"]} | Modelo: {carro["modelo"]} | Ano: {carro["ano"]}")

    print("-----------------------------------------------------------")

def editar_carro():
    placa = input("Digite a placa do carro a ser editado: ")
    
    carro_existente = encontar_carro(placa)

    if carro_existente == None:
        print("\nNão foi encontrado um carro com essa placa.")
        return
    
    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "cor": carro_existente["cor"],
        "modelo": carro_existente["modelo"],
        "ano": carro_existente["ano"]
    }

    print("\nPressione Enter para manter o valor atual.")

    nova_placa = input(f"Placa existente: {carro_existente["placa"]}. Nova placa: ")
    if len(nova_placa) > 0:
        if encontar_carro(nova_placa) != None:
            print("\nJa existe um outro carro com essa placa.")
            return
        
        dicionario_atualizacao["placa"] = nova_placa

    nova_cor = input(f"Cor existente: {carro_existente["cor"]}. Nova cor: ")
    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    novo_modelo = input(f"Modelo existente: {carro_existente["modelo"]}. Novo modelo: ")
    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano = input(f"Ano existente: {carro_existente["ano"]}. Novo ano: ")
    if len(novo_ano) > 0:
        dicionario_atualizacao["ano"] = int(novo_ano)

    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]

    print("\nCarro editado com êxito.")

def deletar_carro():
    placa = input("Digite a placa do carro a ser deletada: ")

    carro_retornado = encontar_carro(placa)

    if carro_retornado ==None:
        print("\nNão foi encontrado um carro com essa placa.")
        return
    
    carros.remove(carro_retornado)
    print("\nCarro deletado.")

def exibir_menu():
    print("\n---------- GERENCIADOR DE GARAGEM ----------")
    print("1 - Cadastrar um carro")
    print("2 - Listar os carros existentes")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "1":
        cadastras_carro()
    elif opcao_escolhida == "2":
        listar_carros()
    elif opcao_escolhida == "3":
        editar_carro()
    elif opcao_escolhida == "4":
        deletar_carro()
    elif opcao_escolhida == "5":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")