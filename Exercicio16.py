#Aula 16 - Exercício 1

'''Crie uma função que receba um valor inteiro e que retorne PAR para numeros pares e IMPAR para numeros immpares'''

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    
    return "Odd"

print(even_or_odd(10))
print(even_or_odd(9))
print(even_or_odd(5))
print(even_or_odd(2))