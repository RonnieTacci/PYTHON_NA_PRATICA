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

print( a + b)
print(round(resultado,1)) # Quantidade de casas decimais

# Relacionais

print(a == 0.1) #comparação
print(a != b) #diferente

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

'''Crie duas variaveis, uma contendo um valor com tres casas decimais,
e outra contendo um valor decimal com duas casas decimais

Multiplique essas daus variaveis e apresente o resultado contendo
duas casas decimais. '''

n1 = 5.378
n2 = 9.22

resultadoDecim = n1 * n2

print (round(resultadoDecim,2))

'''Crie duas variaveis inteiras. Faça todas as operações relacionais apresentadas
na aula, exibindo o resultado de cada comparação.'''

num1 = 10
num2 = 20 

print("comparação: ",num1 == num2) #comparação
print("diferente: ",num1 != num2) #diferente
print("maior que: ",num1 > num2)  #maior que
print("menor que: ",num1 < num2)  #menor que
print("maior ou igual: ",num1 >= num2) #maior ou igual a
print("menor ou igual: ",num1 <= num2) #menor ou igual a

'''Pense na seguinte situação: ano que vem quero viajar,
mas eu so consigo viajar se eu estiver de ferias do trabalho e
tiver conseguido comprar as passagens

Não consegui as ferias no trabalho, mas consegui comprar as passagens.

Se eu fosse utilizar variaveis booleanas do python, e um operador logico
para montar um codigo para exibir se desse jeito eu vou ou não conseguir viajar,
como esse codigo ficaria?'''

ferias_do_trabalho = False
compra_das_passagens = True

viajar_proximoANO = ferias_do_trabalho and compra_das_passagens

print(f"Proximo ano eu irei conseguir viajar: {viajar_proximoANO}")

'''Eu so posso participar de um evento na minha cidade se eu tiver
um convite, ou então, se meu nome estiver na lista de  entrada

Meu nome não esta na lista, mas eu tenho um convite.

Se eu fosse utilizar variaveis booleanas do python, e um operador logico
para montar um codigo para exibir se desse jeito eu vou ou não entrar no evento
como esse codigo ficaria?'''

convite_evento = True
nome_lista = False

entrarNoEvento = convite_evento or nome_lista

print(f"Entrar no local do evento: {entrarNoEvento}")
