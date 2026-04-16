# Estruturas condicionais (if, elif, else)

'''if CONDIÇÃO:
    comando_1
    comando_2
    
CONDIÇÃO -> qualquer operação que, utilizando operadores logicos
e/ou relacionais, resulte em verdadeiro(True) ou falso(False)'''

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Não é considerado adulto ainda.")

print("Fim do programa.")


nota = float(input("Informe sua nota: "))

if nota >= 7.0:
    print("Passou direto!")
elif nota >= 4.0:
    print("Recuperação.")

    nota_recup = float(input("Nova nota de recuperação: "))

    if nota_recup >= 6:
        print("Passou na recuperação, aprovado!")
    else:
        print("Reprovado.")

else:
    print("Reprovado.")

#Exercicios

'''Peça ao usuario para digitar a temparatura atual em Celsius.
Se for maior ou igual a 30, exiba "Esta muito quente!".Se estiver
acima ou igual a 20 e abaixo de 30, exiba "Esta agradavel!Se estives
abaixo de 20 exiba "Esta muito frio!"'''

temperatura = int(input("Informe a temperatura atual em Celsius: "))

if temperatura >= 30:
    print("Esta muito quente!")
elif temperatura >= 20:
    print("Esta agradavel!")
else:
    print("Esta muito frio!")

'''Peça ao usuario para digitar a idade de uma pessoa.Com base nessa idade,
informe o valor da tarifa de tranporte que tera que ser paga.
Se a idade for menos de 6 anos, tarifa sera gratuita. Se for acima ou igual a 6 anos
e abaixo de 18 anos, meia tarifa(5 reais). Se for a partir de 18 anos e abaixo de 60 anos,
tarifa inteira(10 reais). Se for idoso,acisa de 60 anos, tarifa gratuita.'''

idade_tarifa = int(input("Informe sua idade: "))

if (idade_tarifa < 6) or (idade_tarifa > 60):
    print("Tarifa gratuita.")
elif (idade_tarifa >= 6) and (idade_tarifa <18):
    print("Meia tarifa (5 reais) ")
else:
    print("Tarifa inteira (10 reais)")

    
'''Peça ao usuario para digitar um username e uma senha.Considera que o 
usuario correto é "admin" e que a senha correta é python2026.
Se as credenciais estiverem corretas, exiba "Login bem sucedido!.
Do contrario, exiba que as credenciais estao incorretas."'''

userName = input("Informe nome de usuario: ")
senhaClientes = input("Informe senha para login. ")

if (userName == "admin") and (senhaClientes == "python2026"):
    print("Login bem sucedido!")
else:
    print("Credenciais incorretas")