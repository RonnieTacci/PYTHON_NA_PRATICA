#Aula 25 - Exercício 10

def diferenca_idades(listas_idades):
    maior = listas_idades[0]
    menor = listas_idades[0]

    for item in listas_idades:
        if item < menor:
            menor = item
        
        if item > maior:
            maior = item

    diferenca = maior - menor
    tupla_resultado = (menor, maior, diferenca)

    return tupla_resultado

lista_entrada = [75, 22, 5, 44, 12, 99]
print(diferenca_idades(lista_entrada))