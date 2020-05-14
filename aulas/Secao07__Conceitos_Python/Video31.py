# Operadores Relacionais
from sqlalchemy import false

print(100 == 100)  # Igualdade
print(100 != 100)  # Negação
print(false == false)

a = False
b = True
print("(a) é igual a (b): ", a == b)

print()
print()
print(10 > 10)  # Diferente
print(10 >= 10)  # Diferente
print(10 > 10) or (10 != 10)  # Diferente
print(10 >= 10) and (10 != 10)  # Diferente
