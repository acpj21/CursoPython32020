# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.


# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula292.csv'
CAMINHO_CSV.touch()

with CAMINHO_CSV.open('a+') as file:
    file.write('Nome,Idade,Endereço')
    file.write('\n')
    file.write('Luiz Otávio,32,"Av Brasil, 21, Centro"')
    file.write('\n')
    file.write('João da Silva,55,"Rua 22, 44, Nova Era""')
    file.write('\n')

with open(CAMINHO_CSV, 'r') as arquivo:
    # leitor = csv.reader(arquivo)

    # em formato de dicionario
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'])

CAMINHO_CSV.unlink()