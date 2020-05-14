# Módulo da divisão

# print(6 % 2)  # Resto da divisão

# print(3 % 2)

# print(5 % 2)

# print(7 % 3.1)

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2
print()  # Espaço entre os valores
print(divisao)
print(resto)
print()  # Espaço entre os valores
print(num1, "dividido por", num2, "é igual a: ", divisao)
print(num1, "dividido por", num2, "é igual a: %.2f" % divisao)
print("O resto da divisão entre", num1, "e", num2, "é igual a: ", resto)
