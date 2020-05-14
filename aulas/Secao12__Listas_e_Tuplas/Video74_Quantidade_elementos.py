lista = ['Cláudio', 'José', 'Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']
print(lista)

print("---------------------------------------")
print(len(lista))
print(lista[len(lista) - 1])
print(lista[6])
print(lista[-1])

print("---------------------------------------")
lista.insert(5, 'José')
print(lista)
lista.append('José') # Adiciona na última posição
print(lista)

print("---------------------------------------")
print(len(lista))
print(lista.count('José'))
print(lista.index('José'))
