print("========== Exemplo 01 ==========")
"""
class MinhaClasse:
    membro_cls = 0
    def func(self):
        print("O método func() foi invocado")


i1 = MinhaClasse()
i1.func()  # Na função se colocarmos _func (privado)...
# MinhaClasse.func(i1)
"""

print("========== Exemplo 02 ==========")

"""
class MinhaClasse:
    membro_cls = 50
    def __init__(self):
        self.membro_inst = -10
    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1 = MinhaClasse()
i2 = MinhaClasse()
i1.membro_inst = 10
print(i1.membro_inst)
print(i2.membro_inst)

print("i1: "+str(i1.membro_inst))
print("i2: "+str(i2.membro_inst))

print("------------------------")
MinhaClasse.membro_cls = 9
print("i1: "+str(i1.membro_cls))
print("i2: "+str(i2.membro_cls))
"""

print("========== Exemplo 03 ==========")

class MinhaClasse:
    membro_cls = 50
    def __init__(self):
        self.membro_inst = -10
    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1 = MinhaClasse()
i2 = MinhaClasse()

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)
print("------------------------")
i1.membro_cls = 1000  # Comentar essa linha para executar linha abaixo
# MinhaClasse.membro_cls = 1000
print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)
