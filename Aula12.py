# Estrutura de repetição

'''Tambem conhecidas como loops. Um bloco de codigo que pode
ser executado varias vezes, ate uma condição ser atingida.'''

#Principais: for e while

#for -> quando temos uma noção da quantidade de vezes que vamos repetir algo.
#while -> quando queremos repetir ate que uma condição não seja mais satisfeita.

'''Estrutura do for

for INDICE in SEQUENCIA_DE_VALORES:
    comando_1
    comando_2 '''

''' range() -> retorna uma sequencia de valores dentro de uma faixa.
Ex: range(1, 6) retorna [1, 2, 3, 4, 5]'''

somatorio = 0

for i in range(1,6):
    print(i)
    somatorio = somatorio + i  # +=

print(somatorio)

'''Estrutura do while
while CONDIÇÃO:
    comando_1
    comando_2
    comando_3'''

'''OBS: É fundamental que, dentro do bloco de codigo de uma estrutura
while,algo que possa causar uma mudança na condição, para que ela deixe
de ser verdadeira em algum momento. (loop infinito)'''

senha_correta = 2233
senha = int(input("Informe a senha: "))

while senha != senha_correta:
    print("Senha incorreta. Tente novamento.")
    senha = int(input("Informe a senha: "))
print("Acesso liberado.")

#Exercicios

'''Monte um programa que peça, um de cada vez, varios numeros
para o usuario ate que ele digite zero. Ao fiz, mostre a soma de todos
esses numeros que ele digitou.'''

numero_lido = int(input("Digite um numero: "))
Somatorio = 0
while numero_lido != 0:
    Somatorio += numero_lido
    numero_lido = int(input("Digite um numero: "))

print(f"A somatoria dos numeros é: {Somatorio}")

'''Monte um programa que, para um determinado numero informado
pelo usuario(limite), exiba o produtorio dos numeros de 1 ate esse limite'''

limite = int(input("Digite um limite: "))
produtorio = 1

for i in range(1, limite + 1):
    produtorio = produtorio * i

print(f"Resultado produtorio: {produtorio}")

'''Monte um programa que, para um determinado numero informado
pelo usuario(limite), exiba o dobro de cada numero de 1 ate esse limite.
Ex de entrada: 5
Ex de saida:
Dobro de 1: 2
Dobro de 2: 4
Dobro de 3: 6
Dobro de 4: 8
Dobro de 5: 10'''

limiteEX3 = int(input("Informe um numero: "))

for i in range(1,limiteEX3 +1):
    print(f"Dobro de {i}: {i * 2}")
