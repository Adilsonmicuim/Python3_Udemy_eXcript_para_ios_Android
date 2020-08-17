# RETORNO DE VALORES MULTIPLOS

def func():
    return 1, 2


a, b = func()
print(func())
print(a)
print(b)

print("=" * 10, "Empacotamento", "=" * 10)
# Também conhecido como empacotamento
t = (10, 20)
a, b = t

print(a)
print(b)


print("=" * 10, "Outro exemplo", "=" * 10)
def potencia(x):
    quadrado = x ** 2
    cubo = x ** 3
    return quadrado, cubo

q, c = potencia(10)
print(q)
print(c)