#Coleções do Python (lista, append, insert, remove, pop, len)

#Variavel -> guarda apenas um valor por vez
#Coleção -> multiplos valores po vez

'''Principais tipos de coleções:
    Listas: elementos ordenados (com posição) e mutaveis.
    Tuplas: elementos ordenados (com posição) e imutaveis.
    Conjuntos: elementos não ordenados (sem posição) e não podem se repetir.
    Dicionarios: elementos na forma de pares chave-valor.'''

#Lista

animais = ["cachorro", "gato", "coelho"] # ordem 0, 1, 2
print(animais) #print(animais[0]) ->cachorro

lista_mista = [10, "teclado", 2.60]
print(lista_mista[1])

# append(valor)
# insert(posição, valor)
lista_inteiros = [10, 11, 12, 13, 14]

lista_inteiros.append(15)
print(lista_inteiros)

lista_inteiros.insert(2, 11.5)
print(lista_inteiros)

#remove(valor)
lista_inteiros.remove(13)
print(lista_inteiros)

#pop(posição)
lista_inteiros.pop(3)
print(lista_inteiros)

tamanho_lista = len(lista_inteiros)
print(tamanho_lista)


# Tuplas
tupla_int = (10, 20, 30)
print(tupla_int[1])

lista_convertida = list(tupla_int)
lista_convertida[1] = 100
tupla_convertida = tuple(lista_convertida)
print(tupla_convertida)

# Conjuntos

conjunto = {10, 10 , 10, 20 ,25, 50, 50}
print(conjunto)

a= {1, 2, 3}
b = {3, 4, 5}
print(a | b) # união 
print(a & b) # interseção (o que tem em comum)
print(b - a) # o que tem de diferença (ordem importa)

# Dicionarios

dicionario = {
    "nome" : "Ronnie",
    "idade" : 25,
    "estado" : "MG"
}

print(f"Tipo do dicionario: {type(dicionario)}")
print(dicionario)


#Exercicios

'''Crie uma lista chamada paises com alguns nomes de paises dentro dela.
Em sewguida:
- Adicione um novo pais ao fim da lista
- Adicione um novo pais logo antes da posição 1
- Remova um pais pelo nome
- Remova um pais pelo indice
- Mostre o total de paises na lista. '''