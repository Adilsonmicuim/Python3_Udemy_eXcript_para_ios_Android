# FUNÇÃO VARIÁDICA
'''
É toda função capaz de receber quantidades arbitrárias de parâmetros.
'''


def lista_de_argumentos(*lista):
    print(lista)


lista_de_argumentos(1, 2, 3, 4, 5, 6)
lista_de_argumentos("um", "Dois", "Três", "Quatro")



print("")
print("=" * 10, "Outro exemplo", "=" * 10)
def lista_de_argumentos_associativas(**dicionario):
    print(dicionario)


lista_de_argumentos_associativas(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativas(Um=1, Dois=2, Tres=3, Quatro=4)

