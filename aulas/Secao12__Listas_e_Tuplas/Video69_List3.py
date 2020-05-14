lista = [1, 2, 3, 4, 5]
lista = lista + [6]

print(lista)
print(len(lista))
print(lista[0])

# Função append
lista.append(11)
print(lista)

lista.append([12])
print(lista)

del (lista[0])
print(lista)

print(10 * [0])

lista += 10 * [0]
print(lista)
print(50 * "-")
