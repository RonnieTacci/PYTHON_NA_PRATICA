#Aula 22 - Exercício 7

def encontrar_menor(lista):
    menor = lista[0]

    for item in lista:
        if item < menor:
            menor = item
    
    return menor

lista_entrada = [34, 15, 88, 2, 10]
print(encontrar_menor(lista_entrada))

lista_entrada = [34, 15, -88, 2, 10]
print(encontrar_menor(lista_entrada))