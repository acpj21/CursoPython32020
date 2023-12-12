# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

import os

# importa o caminho de forma automática
caminhoExecutavel = os.popen('pwd').read()

# formata o caminho
caminho = os.path.join(caminhoExecutavel)

caminho = caminho.rstrip()

# print(caminhoExecutavel)

for item in os.listdir(caminho):
    print('Item: ', item)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('Imagem: ', imagem)