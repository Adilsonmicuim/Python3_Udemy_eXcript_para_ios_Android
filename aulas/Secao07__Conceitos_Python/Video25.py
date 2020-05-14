# Manipulação de dados


"""
No exemplo abaixo não vamos definir qual é o tipo da variavel
"""
num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

print(num_int)
print(num_dec)
print(val_str)

print("o valor é:", num_int)  # É necessário por a virgula passando o valor para String
print("o valor é:%i" % num_int)  # marcado %i significa inteiro - repara que não tem espaço depois dos dois pontos
print("o valor é: %i" % num_int)  # Agora imprime com espaço
print("o valor é:" + str(num_int))  # Convertendo para string - O + é para concatenar
