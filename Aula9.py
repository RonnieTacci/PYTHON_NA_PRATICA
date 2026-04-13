# Operadores de Python

''' Aritimeticos - usados paa faze calculos matematicos
    Relacionais - usados para comparar valores
    Logicos - usados para combinar condições, normalmente booleanos'''

# Aritimetico

x = 30
y = 3

print( x + y)
print( x ** y) #POTENCIA (X elevado à Y)
print( x // y) #divisão mostrando somente o resultado INTEIRO
print( x % y)  #resto da divisão

a = 0.1
b = 0.2
resultado = a + b

print ( a + b)
print (round(resultado,1))

# Relacionais

print (a == 0.1) #comparação
print (a != b) #diferente

# Logicos

a = True
b = False

print( a and b) # and (E) ambos tem que ser verdadeiro
print(a or b) # or (ou) um ou outro valor tem que ser verdadeiro
print(not a) # invertendo o valor logico


# Exercicios

'''Crie duas variaveis, com valores inteiros.
Faça com essas variaveis todas as operações aritmeticas mostradas na aula.
Armazene os resuldados de cada operação e utilize fstrings para imprimir cada resultado no seguinte modelo:
'Resultado da soma:10'  '''

nuInt1 = 20
nuInt2 = 20

somaInt = nuInt1 + nuInt2
subtacaoInt = nuInt1 - nuInt2
vezesInt = nuInt1 * nuInt2
divisaoInt = nuInt1 / nuInt2

print(f"Resultado da soma: {somaInt}")
print(f"Resultado da subtração: {subtacaoInt}")
print(f"Resultado da multiplicação: {vezesInt}")
print(f"Resultado da divisão: {divisaoInt}")

potenciaInt = nuInt1 ** nuInt2
restoInt = nuInt1 % nuInt2

print(f"Resultado da potencia: {potenciaInt}")
print(f"Resultado do resto da divisão: {restoInt}")
