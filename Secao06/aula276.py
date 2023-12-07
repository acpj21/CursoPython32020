# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

# delta = relativedelta(data_fim, data_inicio)
delta = relativedelta(data_inicio, data_fim)
print(delta)
print(delta.years)
print(delta.months)
print(delta.days)

# delta = data_fim - data_inicio
# delta = timedelta(days=10, hours=2)
# print(data_fim + relativedelta(seconds=59, minutes=10))
# print(data_fim + delta)
# print(data_inicio)
# print(data_fim)
# print(data_inicio > data_fim)
# print(delta.days, delta.seconds)
# print(delta.total_seconds())