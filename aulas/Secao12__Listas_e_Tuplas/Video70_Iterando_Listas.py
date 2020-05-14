# Itera significa percorrer todos os itens
lista_nums = [100, 200, 300, 400]
for item in lista_nums:
    print(lista_nums)

print(50 * "-")
# O cógigo abaixo não funciona
# lista_nums2 = [100, 200, 300, 400]
# for item in lista_nums2:
#     item += 1000
#     print(lista_nums2)

lista_nums2 = [100, 200, 300, 400]
lista_indice = [0, 1, 2, 3]
for item in lista_indice:
    lista_nums2[item] += 1000
    print(lista_nums2)

print(50 * "-")
# Função de nome range
lista_nums3 = [100, 200, 300, 400]
lista_indice = range(4)
for item in lista_indice:
    lista_nums3[item] += 1000
    print(lista_nums3)

print(50 * "-")
lista_nums4 = [100, 200, 300, 400, 500]
for item in range(4):
    lista_nums4[item] += 1000
    print(lista_nums4)

print(50 * "-")
lista_nums4 = [100, 200, 300, 400, 500]
for item in range(len(lista_nums4)):
    lista_nums4[item] += 1000
    print(lista_nums4)

print(50 * "-")
# Função de nome enumerate
lista_nums4 = [100, 200, 300, 400, 500, 600, 700, 800]
for item, indice in enumerate(lista_nums4):
    lista_nums4[item] += 1000
    print(lista_nums4)
