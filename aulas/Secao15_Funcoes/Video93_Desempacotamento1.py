# DESEMPACOTAMENTO
"É a extensão dos elementos contidos numa estrutura"
"Usar um * para lista e tuplas e dois ** para dicionário"

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "Adilson", "Lima", 20
# pessoa(tupla[0], tupla[1], tupla[2])
pessoa(*tupla)

print("")
lista = ["Adilson", "Lima", 20]
pessoa(*lista)

print("")
d = {"nome":"Adilson", "sobrenome":"Lima", "idade":30}
pessoa(**d)