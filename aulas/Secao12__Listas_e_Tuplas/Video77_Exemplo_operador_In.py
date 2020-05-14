a = 10
b = 25
c = 66

x = int(input("Digite um número: "))

if (x == a or x == b or x == c):
    print("Está contido!")
else:
    print("Não está contido.")

print("----------------------")
# if (x in [10, 25, 66]):
if (x in [a, b, c]):
    print("Está contido!")
else:
    print("Não está contido.")

print("----------------------")
cores = ["azul", "amarelo", "branco"]
while True:
    cor = input("Digite uma cor ou 0 para sair! \ncor: ")
    if (cor == "0"):
        break
    elif cor in cores:
        print("Está contido")
        break
else:
    print("Não está contido")
