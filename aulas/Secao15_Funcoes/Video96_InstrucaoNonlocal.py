# INSTRUÇÃO NONLOCAL

" É a instrução que permite acessar membros não globais e não locai, membros contidos no escopo esterno."


def func():

    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()

func()



print("")
print("=" * 10, "Outro exemplo", "=" * 10)
x = 10
def funcX():
    global x
    return x

print(funcX())
