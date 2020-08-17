# DESEMPACOTAMENTO

lista = [11, 10, 12]

def func(a, b, c):
    print(a)
    print(b)
    print(c)


lista.sort()
func(*lista)



print("")
print("=" * 10, "Exemplo 2", "=" * 10)
tupla = 11, 10, 12

def func(a, b, c):
    print(a)
    print(b)
    print(c)


l = [*tupla]
l.sort()  # Organizar o elementos contido na lista
func(*l)



print("")
print("=" * 10, "Exemplo 3", "=" * 10)
tupla = 11, 10, 12

def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(**dict(zip(("a", "b", "c"), lista)))