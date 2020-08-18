# EXCEÇÕES
"EXCEÇÃO é todo o desvio da regra geral (Dicionário Aurélio)"

"""
TRATAMENTO DE EXCEÇÕES
É todo código que identifica erros e implementa uma solução evitando que a aplicação seja finalizada.
"""


"""
LEVANTAMENTO DE EXCEÇÕES
É todo código que ao perceber um problema cria uma exceção avisando o programador.
"""

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não é possível dividir um n° por 0")