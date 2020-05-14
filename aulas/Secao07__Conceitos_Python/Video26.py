# Ponto Flutuante

num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

print(num_int)
print(num_dec)
print(val_str)

print("o valor é:", num_int)  # É necessário por a virgula passando o valor para String
print("o valor é:%i" % num_int)  # marcado %i significa inteiro - repara que não tem espaço depois dos dois pontos
print("o valor é: %i" % num_int)  # Agora imprime com espaço
print("o valor é:" + str(num_int))  # Convertendo para string, O + é para concatenar

print("Concatenando decimal:", num_dec)
print("Concatenando decimal: %.10f" % num_dec)  # com 10 casas decimais
print("Concatenando decimal:" + str(num_dec))

print("Concatenando strings:", val_str)
print("Concatenando strings: %s" % val_str)
print("Concatenando strings: " + val_str)
