#Aula 23 - Exercício 8

def seculo(ano):
    parte_inteira = ano // 100
    parte_decimal = ano % 100

    if parte_decimal > 0:
        parte_inteira += 1

    return parte_inteira

print(f"Seculo: {seculo(1999)}")
print(f"Seculo: {seculo(2026)}")
print(f"Seculo: {seculo(1978)}")
print(f"Seculo: {seculo(1500)}")