# MÉTODO CONSTRUTOR

"""
É invocado automaticamente pelo Python a cada novo objeto criado
"""


def __init__():
    pass


print("============================")


class Pessoa:
    def __init__(self):
        pass


Pessoa()

print("============================")


class A:
    def __init__(self):
        print(id(self))


A()


print("============================")


class B:
    def __init__(self):
        print(id(self))


b = B()
print(id(B))