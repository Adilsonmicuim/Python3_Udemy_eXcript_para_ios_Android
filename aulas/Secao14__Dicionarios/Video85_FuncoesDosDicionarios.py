telefone = {}
telefone = {}
telefone = {
    30301122: "Pericles",
    22547877: "Menelau",
    33381245: "Atreu",
    63458899: "Tieste"
}
print(telefone)
print(len(telefone))

print('---'*10)


del(telefone[30301122])
print(telefone)
print(telefone.keys())
print(telefone.values())
print(telefone.popitem()) #Retorna o elmento e já exclui ALEATÓRIAMENTE do dicionáro
print(telefone)


print('*****'*10)
# Este número esta contido dentro deste dicionário
print(33381245 in telefone)