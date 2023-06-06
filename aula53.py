lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
lista_enumerada0 = list(enumerate(lista))
tupla_enumerada0 = tuple(enumerate(lista))

for nome in lista:
    print(nome)

print(' ')
print(' ')

for item in lista_enumerada:
    indice, nome = item
    print(indice, nome)

print(' ')
print(' ')

for item in lista_enumerada0:
    indice, nome = item
    print(indice, nome)

print(' ')
print(' ')

for item in tupla_enumerada0:
    indice, nome = item
    print(indice, nome)