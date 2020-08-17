# ARGUMENTOS
'''
POSICIONAL x NOMEADOS
'''

# Definimos 4 parâmetros para a função.
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome, sobrenome, idade, sexo))

# POSICIONAL
dados_pessoais('Adilson', 'Lima', 30, 'M')

print("")
# Em seguida vamos colocar o nome do parâmetro que recebe determinado valor.
# NOMEADO
dados_pessoais(nome="Adilson", sobrenome="Lima", idade=30, sexo=True)
