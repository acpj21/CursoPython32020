# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fmt_1 = '%d/%m/%Y'
fmt_2 = '%d/%m/%Y %H:%M'
fmt_3 = '%d/%m/%Y %H:%M:%S'
data = datetime(2022, 12, 13, 7, 59, 23)

print(data.strftime(fmt_1))
print(data.strftime(fmt_2))
print(data.strftime(fmt_3))