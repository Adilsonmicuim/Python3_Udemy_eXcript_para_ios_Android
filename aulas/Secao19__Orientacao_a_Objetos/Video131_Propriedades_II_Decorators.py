# DECORATORS

"""
O DECORADOR DE MÉTODO adiciona funcionalidades ao método sem alterar a sua implementação.
"""


class A:
    def __init__(self):
        self.var = 0

    @property
    def var(self):
        print("Valor esta sendo lido")
        return self._var

    @var.setter
    def var(self, x):
        print("Valor esta sendo escrito")
        self._var = x


# var = property(fget=_get_var, fset=_set_var)


a = A()
a.var = 10
t = a.var
# print(a.var)
