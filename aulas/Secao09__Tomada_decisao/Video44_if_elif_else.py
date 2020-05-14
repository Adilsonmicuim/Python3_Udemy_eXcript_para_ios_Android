idade = int(input("Informe sua idade: "))
if (idade <= 0):
    print("Sua idade não pode ser 0 ou menor a 0!")
elif (idade > 150):
    print("Sua idade não pode ser maior do que 150 anos!")
elif (idade < 18):
    print("Você precisa ter mais de 18 anos!")
else:
    print("Idade aceita")