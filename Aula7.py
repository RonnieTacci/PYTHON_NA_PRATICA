# Exercício de Fixação- Variaveis

'''Crie duas variaveis, uma chamada nome e outra idade. 
Atribua a elas o nome e idade de alguiem, e mostre esas informações na tela no seguinte formato:
Me chamo [nome] e tenho [idade] anos.'''

nome = "Ronnie"
idade = 25

print(f"Me chamo {nome} e tenho {idade} anos.")


'''Crie duas variaveis: nome e animal, contendo o nome e o animal de estimação de alguem.
Em seguida, mostre essas informações em tres formas de exibir texto com variaveis
O [nome] tem um [animal]'''


nome = "Gustavo"
animal = "gato"

print("O", nome, "tem um", animal)
print(f"O {nome} tem um {animal}")
print("O " + nome + " tem um " + animal)

'''Crie uma constante chamada PAIS com o valor "Brasil", uma variavel chamada nome com o nome de alguem,
e outra chamada idade com a idade dessa pessoa especifica. Exiba essas informações no seguinte formato:
[nome] mora no pais [PAIS] e tem [idade] anos'''

PAIS = "Brasil"             #variaveis com LETRAS MAIUSCULAS sao constantes
nome = "Saulo"
idade = 40

print(f"{nome} mora no pais {PAIS} e tem {idade}")