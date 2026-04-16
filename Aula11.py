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