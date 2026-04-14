# Input de dados (entrada)

nome = input("Informe seu nome: ")
print(f"Bme-vindo {nome}")

idade = input("Informe sua idade: ")        
print(type(idade))
print(f"Sua idade é {idade}, permissão para entrar.")

# idade = int(input("Informe sua idade: ")) ou variavel = float(input("Informe sua idade: "))

#Exercicios de fixação

'''Peça ao usuario para digitar o nome dele e exiba uma saudação personalizada.
Ex: "Ola, Fulano! Seja bem vindo!" '''

nome_usuario = input("Informe seu nome: ")
print(f"Ola, {nome_usuario}! Seja bem vindo!")

'''Peça dois numeros inteiros ao usuario, some os dois e apresente o resultado
em uma frase no formato abaixo:
Ex: "O resultado é 20" '''

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))
n3 = n1 + n2

print(f"O resultado é {n3}")

'''Peça duas notas ao usuario (podem ter casas decimais) e
mostre a meidia delas'''

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A sua média foi: {media}")

'''Peça ao usuario o nome, idade e estado dele, e
exiba uma frase completa no formato abaixo:
Ex: "Fulano tem 21 anos e mora no estado Mato Grosso"'''

nomeUSUARIO = input("Informe seu nome: ")
idadeUSUARIO = int(input("Informe sua idade: "))
estadoUSUARIO = input("Informe seu Estado: ")

print(f"{nomeUSUARIO} tem {idadeUSUARIO} anos e mora no estado {estadoUSUARIO}")