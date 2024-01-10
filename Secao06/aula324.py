# from time import sleep
# print('Hello')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('World!')

from time import sleep
from threading import Thread


class MeuThead(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()
   
    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThead('Thread 1', 5)
t1.start()

t2 = MeuThead('Thread 2', 2)
t2.start()


for i in range(20):
    print(i)
    sleep(1)