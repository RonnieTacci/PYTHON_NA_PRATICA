import math

# sqrt -> raiz quadrada
# nome_da_biblioteca.nome_da_funcao(parametros)

print("Utilizando a função sqrt:")

raiz_quadrada = math.sqrt(25)
print(f"Raiz quadrada de 25 = {raiz_quadrada}")

raiz_quadrada = math.sqrt(16)
print(f"Raiz quadrada de 16 = {raiz_quadrada}")

raiz_quadrada = math.sqrt(6)
print(f"Raiz quadrada de 6 = {raiz_quadrada}")

# pow -> calculo de potencia

print("\nUtilizando a função pow")

potencia = math.pow(10, 3)
print(f"10 elevado a 3 = {potencia}")

potencia = math.pow(3, 4)
print(f"3 elevado a 4 = {potencia}")

potencia = math.pow(4, 6)
print(f"4 elevado a 6 = {potencia}")

# ceil -> arredondar numero decimal para cima,
# voce decide que vai arredondar o numero para
# o inteiro mais próximo de cima

# floor -> arredondar numero decimal para baixo
# voce decide que vai arredondar o numero para
# o inteiro mais próximo de baixo

# round -> arredondar numero decimal para inteiro
# mais proximo a funcao decide isso por você

print("\nUtilizando as funções ceil e floor")

arr_cima = math.ceil(4.678)
print(f"4.678 arredondado para cima = {arr_cima}")

arr_baixo = math.floor(4.678)
print(f"4.678 arredondado para baixo = {arr_baixo}")

arr_round = round(4.678)
print(f"4.678 arredondado com round = {arr_round}")

print("\nUtilizando a constante pi")

raio = 4
area = math.pi * math.pow(raio, 2)
print(f"Area calculada do circulo = {area} m2")
print(f"Area arredondada do circulo = {round(area)} m2")