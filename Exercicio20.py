#Aula 20 - Exercício 5

'''Encontrar a agulha no palheiro
Escreva uma função findNeedle() que leva uma lista cheia de itens, mas contendo uma "agulha"
Após a sua função encontrar a agulha, ela deverá retornar uma mensagem(str) que diz:
"Encontrou a agulha na posição"'''

palheiro_list = ["hay", "junk", "hay", "hay", "moreJunk", "agulha", "randomJunk"]

def encontrar_agulha(palheiro):
    position = 0

    for element in palheiro:
        if element == "agulha":
            break

        position += 1

    return f"Encontrou a agulha na posição {position}"

print(encontrar_agulha(palheiro_list))