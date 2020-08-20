# OBJETO CLASSE

"""
As CLASSES são utilizadas para criar objetos e em Python as mesmas também são objetos.
"""

# OBJETO CLASSE
# INSTÂNCIA DE CLASSE

"""
Há diversos benefícios na utilização de CLASSE OBJETO mas que, talvez, 
não seja muito fácil reconhecê-los num primeiro momento.
"""

print(" Usando terminal IDE.py")
class MinhaClasse:
    pass


obj = MinhaClasse()
type(obj)

type(MinhaClasse)

obj.__class__

MinhaClasse.__class__

MinhaClasse.__dict__

from pprint import pprint
pprint(MinhaClasse.__dict__)
pprint(obj.__dict__)
