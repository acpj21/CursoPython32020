# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

# Ao invés de usar ponto como separador, usa-se o underline(_)
valor_emprestimo = 1_000_000

data_fmt = '%d/%m/%Y %H:%M:%S'
data_inicio_emprestimo = datetime(2020, 12, 20, 9, 00, 00)
string_data_inicio_emprestimo =  data_inicio_emprestimo.strftime(data_fmt)
mensagem_inicio = f'Data Inicio empréstimo: {string_data_inicio_emprestimo}'

#Tempo de duração do emprestimo
delta = relativedelta(years=5)
data_final_emprestimo = data_inicio_emprestimo + delta

string_data_final_emprestimo =  data_final_emprestimo.strftime(data_fmt)
mensagem_final = f'Data Final empréstimo: {string_data_final_emprestimo}'

data_parcelas = []

data_parcela = data_inicio_emprestimo

while data_parcela < data_final_emprestimo:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)


numero_parcelas = len(data_parcelas)

valor_parcela = valor_emprestimo / numero_parcelas

for data in data_parcelas:
    print(data.strftime(data_fmt), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_emprestimo:,.2f} para pagar '
    f'em {delta.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)