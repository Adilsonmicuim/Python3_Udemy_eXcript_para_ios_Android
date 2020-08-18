# CRIAÇÃO DE OBJETOS

"""
INSTÂNCIA: É cada um dos objetos criados durante a execução do programa (Dicionário Aurélio).
"""

"""
CLASSE: É o projeto de um Objeto.
OBJETO: É a execução do código de uma classe.
INSTÂNCIA: É sinônimo de Objeto.
"""

'''
No Python todo OBJETO possui um ID composto por um número inteiro não negativo.
'''


class Pessoa:
    pass


# Criamos dois OBJETOS a partir da mesma classe
p1 = Pessoa()  # Para criar uma instância deve-se usar o nome da classe
p2 = Pessoa()  # Toda instância precisa associar a uma variável.

print(id(p1))
print(id(p2))
