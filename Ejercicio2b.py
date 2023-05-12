
import threading
import time
import random
import logging

from ColaFIFO import ColaFIFO

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class ColaFIFOcero(ColaFIFO):
    def __init__(self):
        super().__init__()

    def extraer(self):
        while self.cola_vacia:
            print("cola vacia")
            pass
        return ColaFIFO.extraer(self)


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
    # hilos = []
    cola = ColaFIFOcero()
   # cola = ColaFIFO()

    productor = Productor(cola, 2)
    consumidor = Consumidor(cola, 2)

    logging.info(f'Arrancando productor {productor.name}')
    productor.start()

    logging.info(f'Arrancando consumidor {consumidor.name}')
    consumidor.start()

    productor.join()
    consumidor.join()




if __name__ == '__main__':
    main()

"""
Probar
"""