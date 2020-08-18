def input_float(msg):
    # Enquanto valor não for correto digite outro valor
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número inválido.")


num1 = input_float("Digite o primeiro número: ")
num2 = input_float("Digite o segundo número: ")

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Não é possível dividir um n° por 0")
