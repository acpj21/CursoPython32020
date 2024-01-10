# from time import sleep
# print('Hello')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('World!')

# from time import sleep
# from threading import Thread


# class MeuThead(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()
   
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThead('Thread 1', 5)
# t1.start()

# t2 = MeuThead('Thread 2', 2)
# t2.start()


# for i in range(20):
#     print(i)
#     sleep(1)

# from time import sleep
# from threading import Thread


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(.5)

from time import sleep
from threading import Thread


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()
t1.join()

# while t1.is_alive():
#     print('Esperando a thead.')
#     sleep(2)

print('Thread acabou!')
