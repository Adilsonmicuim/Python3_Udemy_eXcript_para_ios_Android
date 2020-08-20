# ENCAPSULAMENTO

""" É o isolamento do código """

"""
INTERFACE PÚBLICA é o conjunto de métodos públicos para acessar os recursos e funcionalidades do código encapsulado.
"""


class Retangulo:

    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura

    def area(self):
        return self.l * self.a


r = Retangulo(10, 5)
print(r.area())
