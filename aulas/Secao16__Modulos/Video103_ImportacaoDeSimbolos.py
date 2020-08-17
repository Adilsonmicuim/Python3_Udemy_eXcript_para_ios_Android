#MÓDULOS

" A IMPORTAÇÃO DE SÍMBOLOS copia atributos de um módulo diretamente à tabela de símbolos local"

"A partir deste módulo import esse símbolo: from modulo import simbolo"

from math import pi, e
from math import sqrt

print(sqrt(9))

print(pi)
print(e)


print("")
print("")
def func():
    from math import factorial
    print(factorial(5))

func()