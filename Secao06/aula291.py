from pathlib import Path
# from shutil import rmtree

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent)

# print(caminho_arquivo.parent.parent)

# # Cria caminho / arquivo

# 

# arquivo.touch()

# print(arquivo)

# # Escrever Texto no arquivo
# arquivo.write_text('Olá Mundo!')
# arquivo.write_text('Olá de novo!')
# print(arquivo.read_text())

# Apagar aarquivo = Path(__file__).parent / 'arquivo.txt'
# arquivo.unlink()

# caminho_arquivo = Path(__file__).parent / 'arquivo.txt'
# caminho_arquivo.write_text('')

# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha \n')
#     file.write('Outra linha \n')

# print(caminho_arquivo.read_text())

caminho_arquivo = Path(__file__).parent / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá mundo!')
caminho_arquivo.unlink()

caminho_pasta = Path().parent / 'Python é legal'

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_Arquivo = subpasta / 'arquivo.txt'
outro_Arquivo.touch()
outro_Arquivo.write_text('Hey')

mais_Arquivo = caminho_pasta / 'arquivo.txt'
mais_Arquivo.touch()
mais_Arquivo.write_text('Hey')

# caminho_pasta.rmdir()
files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file{i}.txt'
    
    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+') as text_file:
        text_file.write('Olá mundo \n')
        text_file.write(f'file{i}.txt')

# rmtree(caminho_pasta)


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('DIR: ', file)
            file.unlink()


rmtree(caminho_pasta)