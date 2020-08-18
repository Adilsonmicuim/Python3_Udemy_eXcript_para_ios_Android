def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e)) # Instância da exceção
        print(e.args) # Argumentos da exceção: Mensagens
        print(e) # __str__ mensagens

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except (TypeError, NameError) as e:
        print(type(e)) # Instância da exceção
        print(e.args) # Argumentos da exceção: Mensagens
        print(e) # __str__ mensagens
        print("TypeError ou NameError")


# TypeError
erro("int + int")

# NameError
erro("a")

print("")
# ValueError
# erro("int('a')")

# ZeroDivisionError
# erro("5/0")
print("A Aplicação foi finalizada")