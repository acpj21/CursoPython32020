"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
print(lista)
lista.append(50)
print(lista)
lista.pop()
ultimo_valor = lista.pop(2)
print(lista, 'Removido,', ultimo_valor)
lista.append(60)
print(lista)
lista.append(70)
print(lista)
lista.pop()
ultimo_valor = lista.pop(2)
print(lista, 'Removido,', ultimo_valor)