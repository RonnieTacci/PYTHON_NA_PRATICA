#Aula 18 - Exercício 3

'''Nesta tafera vocé recebe um numero e tranforma ele em negativo, mas talves o numero ja esteja negativo.'''

def num_negativo( numero ):
    if numero > 0:
        return numero * -1
    
    return numero
    

print(num_negativo(8))
print(num_negativo(1))
print(num_negativo(0))
print(num_negativo(-10))