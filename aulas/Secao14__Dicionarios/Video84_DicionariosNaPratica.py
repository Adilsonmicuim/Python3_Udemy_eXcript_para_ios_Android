'''
Todos os elementos contidos dentro de duas chaves {}, para o python será um elemento pertencente a um dicionário.
'''

{}  # Dicionário vazio
type({})
d1 = {}
print(type(d1))

print('--' * 10)

d2 = dict()
print(d2)

print('--' * 10)

d1['aaa'] = 1000
d1['bbb'] = 2000
print(d1)

print('--' * 10)

d2 = {1.1:'Teste01', 2.2:'Teste02', 3:'Teste03'}
print(d2)
print(d2[2.2])
