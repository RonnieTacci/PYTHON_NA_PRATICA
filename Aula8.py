# Tipos de dados


''' str : dados textuais (strings)
    int : numeros inteiros (sem casa decimal)
    float : numeos decimais ( com pate decimal, ponto)
    bool : valores logicos (True e False)'''

#exemplos

meu_texto = "Minha palavra"
print(type(meu_texto))      # ( type -> mostrou o tipo da variavel)
print(meu_texto)

variavel_int = 100
print(variavel_int)


print(type(100.50))

esta_chovendo = True
luzAcesa = False

print(esta_chovendo)
print(luzAcesa)



#exercicios

'''Crie 4 variaveis com os seguintes nomes:
 - nome
 - idade
 - altura
 - uma variavel booleana para representar se gosta de programar
 
 Preencha essas variasveis com informações de alguem,
 em seguida exiba o tipo de cada variavel.'''

nome = "Ronnie Tacci"
idade = 25
altura = 1.70
gostarDeProgramar = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(gostarDeProgramar))


''' Usando as mesmas variasveis do exercicio anterior,
exiba uma frase com todas essas informações usando f-string'''

print(f"O meu nome é {nome}, eu tenho {idade}, {altura} de altura e se eu gosto de programar:{gostarDeProgramar}")