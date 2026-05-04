#Aula 24 - Exercício 9

'''Regras:
    Cada par de pedaços da listadevem estar em um tupla
    Cada pedaço dentro da tupla deve ser uma string
    Os elementos de um par de pedaços devem seguir a ordem original da lista de entrada'''

#Exemplo de tupla dentro de uma lista

lista_com_tupla = [("Leão", "Leoa"), ("Galo", "Galinha"), ("animais", "plantas")]

print(lista_com_tupla)
print(type(lista_com_tupla[0])) # type -> mostrou o tipo da variavel

tamanho_lista = len(lista_com_tupla)
print(f"Tam. da lista: {tamanho_lista}")


#Exemplo slicing- dividindo uma lista

minha_lista = ["Brasil", "Argentina", "Canadá", "Peru", "Japão"]

primeiro_pedaco = minha_lista[:2]
print(f"Primeiro pedaço: {primeiro_pedaco}")

segundo_pedaco = minha_lista[2:]
print(f"Segundo pedaço: {segundo_pedaco}")

#Exemplo join- separador

separador = "/"
lista_cores = ["azul", "verde", "vermelho"]
string_resultado = separador.join(lista_cores)

print(string_resultado)

def partlist(lista_entrada):
    lista_resultante = []
    tam_lista = len(lista_entrada)
    espaco_lit = " "

    for limite in range(1, tam_lista):
        pedaco_comeco = lista_entrada[:limite]
        pedaco_fim = lista_entrada[limite:]

        pedaco_comeco_str = espaco_lit.join(pedaco_comeco)
        pedaco_fim_pedaco_str = espaco_lit.join(pedaco_fim)

        tupla = (pedaco_comeco_str, pedaco_fim_pedaco_str)
        lista_resultante.append(tupla)

    return lista_resultante

lista_entrada = ["az", "toto", "picaro", "zone", "kiwi"]

print(partlist(lista_entrada))