opcoes_aceitas = ['i', 'a', 'l']

lista = []

while True:
    print(' ')
    print('Selecione uma opção: ')
    print(' ')
    opcao = input('[i]inserir [a]pagar [l]istar: ')
    print(' ')

    if len(opcao) > 1:
        print(' ')
        print('Favor digitar apenas uma letra.')
        print(' ')
        continue

    if opcao not in opcoes_aceitas:
        print(' ')
        print('Opção não aceita, favor digitar apenas uma letra.')
        print(' ')
        continue

    if opcao == 'l':
        if len(lista) > 0:
            print(lista)
        else:
            print(' ')
            print('Nada para listar.')
            print(' ')
    elif opcao == 'i':
        inserir_item_lista = input('Qual o item a inserir? ')

        if len(inserir_item_lista) == 0:
            print(' ')
            print('Favor digitar pelo menos uma letra.')
            print(' ')
            continue

        lista.append(inserir_item_lista)

        print(' ')
        print('Item inserido: ', inserir_item_lista)
        print(' ')
        
    elif opcao == 'a':
        if len(lista) > 0:
            apagar_item_lista = input('Qual o item a apagar? ')
        else:
            print(' ')
            print('Nada para apagar.')
            print(' ')
            continue

        if len(apagar_item_lista) == 0:
            print(' ')
            print('Favor digitar pelo menos uma letra.')
            print(' ')
            continue

        if apagar_item_lista in lista:
            lista.remove(apagar_item_lista)
            print(' ')
            print('Item apagado: ', apagar_item_lista)
            print(' ')
        else:
            print(' ')
            print('Item não encontrado.')
            print(' ')