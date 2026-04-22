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

