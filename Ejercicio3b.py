
import threading
import time
import random
import logging

from ColaFIFOmax import ColaFIFOmax

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class ColaFIFOExtendida(ColaFIFOmax):
    def __init__(self, size):
        super().__init__(size)

    def insertar(self, dato):
        while self.cola_llena:
            print("cola llena")
            pass
        ColaFIFOmax.insertar(self, dato)

    def extraer(self):
        while self.cola_vacia:
            print("cola vacia")
        return ColaFIFOmax.extraer(self)

class Productor(threading.Thread):
    def __init__(self, cola, retardo):
        super().__init__()
        self.cola = cola
        self.retardo = retardo

    def run(self):
        while True:
            self.cola.insertar(random.randint(0,100))
            logging.info(f'esta produciendo {self.cola.ultimo()}')
            time.sleep(self.retardo)


class Consumidor(threading.Thread):
    def __init__(self, cola, retardo):
        super().__init__()
        self.cola = cola
        self.retardo = retardo

    def run(self):
        while True:
            elemento = self.cola.extraer()
            logging.info(f'consumio el elemento {elemento}')
            time.sleep(self.retardo)


def main():
    hilos = []
    cola = ColaFIFOExtendida(2)

    productor = Productor(cola, 2)
    consumidor = Consumidor(cola, 2)
    hilos.append(productor)
    hilos.append(consumidor)
    logging.info(f'Arrancando productor {productor.name}')
    productor.start()
    logging.info(f'Arrancando consumidor {consumidor.name}')
    consumidor.start()

if __name__ == '__main__':
    main()

