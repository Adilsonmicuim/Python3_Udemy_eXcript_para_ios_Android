# VISIBILIDADE DOS MEMBROS

"""
É um recurso da orientação a objetos que impede o acesso externo
a membros de uso exclusivamente interno ao objeto.
"""

"""
A OCULTAÇÃO DE MEMBROS não ocorre na prática, o Python não possui este recurso.
"""

"""
MEMBROS DE USO INTERNO
Membros de uso exclusivamente interno ao objeto deverão ter seus nomes precedidos po UM "underline"
publico = 0
_restrito = 0
"""

publico = 0
_restrito = 0

print("======================")


class Pessoa:
    def __init__(self):
        self._teste = 0

    def _func(self):
        pass


print("======================")


class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.__var = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self._altura = num
        self.__var = 456

    def set_largura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é valida: {}".format(num))
        self._largura = num

    def get_area(self):
        return self._altura * self._largura


r = Retangulo(largura=5, altura=5)
r = Retangulo(largura=5, altura=5)
