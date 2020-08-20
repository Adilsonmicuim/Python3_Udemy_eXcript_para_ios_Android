# PROPRIEDADES

"""
É um recurso para declaração de membros públicos que permite invocar métodos
na leitura e escrita de valores.
"""
I = 10

"""
# escrita
instancia.attr = 0

# leitura
x = instancia.attr
"""


# FUNÇÃO property
# property(fget, fset, fdel, doc)

class A:
    def __init__(self):
        self.var = 0

    def get_var(self):
        print("Valor esta sendo lido")
        return self._var

    def set_var(self, x):
        print("Valor esta sendo escrito")
        self._var = x

    var = property(fget=get_var, fset=set_var)


a = A()
# a.set_var(1000)
# print(a.get_var())
a.var = 10
print(a.var)
