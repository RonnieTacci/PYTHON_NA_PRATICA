#Funções do Python

#Funções

'''São blocos de codigos separados e reutilizaveis, cada um tendo
um objetivo e/ou tarefa em especifico.

Estrutura de uma função no Python

def NOME_FUNCAO(PARAMETRO_1, PARAMETRO_2):
    comando_1
    comando_2
    comando_3
    
    return VALOR_RETORNO
    
Variações

Sem parametro, sem retorno
def NOME_FUNCAO():
    comando_1
    comando_2
    comando_3
    
Com parametro, sem retorno
def NOME_FUNCAO(PARAM_1,PARAM_2):
    comando_1
    comando_2
    comando_3
    
Sem parametros, com retorno
def NOME_FUNCAO():
    comando_1
    comando_2
    comando_3
    
    return VALOR_RETORNO''' 

# Exemplos

def exibir():
    print("Executando a função exibir()")
    print("Execução finalizada.")

exibir()

def produto(x, y):
    resultado = x * y
    return resultado

multiplicacao = produto(4, 8)
print(f"Resultado de 4 vezes 8: {multiplicacao}")

def exibir_frase(nome, altura, linguagem):
    print(f"{nome} tem {altura}m e programa em {linguagem}.")
exibir_frase("Ronnie", 1.71, "Python")

def calcular_media(numero_aluno):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    media = round(media, 1)

    print(f"Média do aluno {numero_aluno}: {media}")

calcular_media(1)
calcular_media(2)

def calcular_veloc_media(distancia, tempo):
    resultado = distancia / tempo
    resultado = round(resultado,2)

    return resultado

distancia = float(input("Informe a distancia em (km): "))
tempo = float(input("Informe o tempo em (h): "))

vel_media = calcular_veloc_media(distancia, tempo)

print(f"Velocidade média: {vel_media} km/h")

def notas_aprovados(lista_notas):
    lista_aprovados = []

    for nota in lista_notas:
        if nota >= 7.0:
            lista_aprovados.append(nota)
    
    return lista_aprovados

lista = [10.0, 4.4, 7.1, 5.9, 9.1]
lista_resultante = notas_aprovados(lista)

print("Notas aprovadas")
print(lista_resultante)