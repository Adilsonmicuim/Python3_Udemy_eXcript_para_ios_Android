# Exemplo 1
s = 'Iterando Strings'

for c in s:
    print(c)

# Exemplo 2
y = 'Iterando Strings'
indice = 0
while indice < len(y):
    print(indice, y[indice])
    indice += 1

# Exemplo 3
for k, v in enumerate('Iterando Strings'):
    print(k, v)
