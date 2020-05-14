acao = int(input("Digite '1' para sim e '2' para não: "))

if (acao == 1):
    print("Você disse sim!")

elif (acao == 2):
    print("Você disse não!")

elif (acao != 1 and acao != 2):
    print("Escolha novamente!")
