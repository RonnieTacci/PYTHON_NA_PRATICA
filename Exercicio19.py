#Aula 19 - Exercício 4

'''Considere uma array/lista de ovelhas onde algumas ovelhas podem estar faltando em seus lugares.
Precisamos de uma função que conte o numero de ovelhas presentes no array(True siginifica presente)'''

def count_sheeps(sheep):
    count = 0

    for item in sheep:
        if item == True:
            count += 1


    return count




input_list = [
    True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True
]

print(count_sheeps(input_list))