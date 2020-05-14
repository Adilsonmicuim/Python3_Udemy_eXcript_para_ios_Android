lista = ['bbb', 'ccc', 'ddd']

print(lista)
print(lista[0])

print("--------------------------------")
print(lista.sort())
lista.append('eee')
print(lista)

print("--------------------------------")
lista.insert(0, 'aaa')
print(lista)

# print("--------------------------------")
# lista.clear()
# print(lista)

# print("--------------------------------")
# lista.pop(0)
# print(lista)

print("--------------------------------")
del(lista[::2])
print(lista)

