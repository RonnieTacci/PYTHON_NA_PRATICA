#Aula 21 - Exercício 6


def invert(list):
    inverted_list = []

    for item in list:
        inverted_item = item * -1
        inverted_list.append(inverted_item)

    return inverted_list

input_list = [1, 2, 3, 4, 5]
print(invert(input_list))