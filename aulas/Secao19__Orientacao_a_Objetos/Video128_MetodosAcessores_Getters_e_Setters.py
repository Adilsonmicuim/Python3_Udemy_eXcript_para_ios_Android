"""
São métodos utilizados na construção da interface pública (Interface de acesso).
"""

# MÉTODOS GETTERS sempre retornam valores
# GET significa o retorno de dados

# MÉTODOS SETTERS sempre recebem valores por parâmetro
# SET significa a atribuição de valor

"""
MÉTODOS ASSESSORES também garantem a integridade das informações internas ao objeto
"""

"""
get_ + atributo >>> get_ + estudo
    get_estudo()
    
set_ + atributo >>> set_ + estudo
    set_estudo()
"""


class Retangulo:

    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self.altura = num

    def set_largura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é valida: {}".format(num))
        self.largura = num

    def get_area(self):
        return self.altura * self.largura


r = Retangulo(largura=10, altura=5)
