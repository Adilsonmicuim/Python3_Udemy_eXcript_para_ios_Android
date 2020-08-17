'''
PARÂMETRO: É uma variável declarada entre os parêntesis () de uma função.
'''

'''
ARGUMENTO vs PARÂMETRO: Conceitos iguais usados em situações diferentes. 
Quando definimos uma função definimos uma lista de PARÂMETROS que deve ser passado, e quando vamos invocar essa função 
vamos dizer os ARGUMENTOS que são passado para esta função. 
'''


def soma(x, y):
    Total = x + y
    print("Total da soma é: ", Total)

soma(10, 20)
soma(25, 25)
