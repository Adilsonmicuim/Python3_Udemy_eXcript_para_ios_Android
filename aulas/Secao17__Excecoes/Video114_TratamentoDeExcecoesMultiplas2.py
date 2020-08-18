def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


# TypeError
erro("int + int")

# NameError
erro("a")

# ValueError
erro("int('a')")

# ZeroDivisionError
erro("5/0")
