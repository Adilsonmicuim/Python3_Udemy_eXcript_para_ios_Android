# FUNÇÕES ANINHADAS
# Declaração de uma função no topo de outra função.

def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()

func()
