import threading
import time
import random
import logging

from ColaFIFOmax import ColaFIFOmax

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class ColaFIFOConcurrente(ColaFIFOmax):
    def __init__(self, size):
        super().__init__(size)
        self.lock = threading.Lock()

    def extraer(self):
        while self.cola_vacia:
           logging.info(f'cola vacia {threading.current_thread().name}')
           pass
    #    time.sleep(random.randint(0,1))
        self.lock.acquire()
        try:
            return ColaFIFOmax.extraer(self)
        finally:
            self.lock.release()

    def insertar(self, dato):
        while self.cola_llena:
            logging.info(f'cola llena {threading.current_thread().name}')
        pass
     #   time.sleep(random.randint(0,1))
        self.lock.acquire()
        try:
            ColaFIFOmax.insertar(self, dato)
        finally:
            self.lock.release()


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
    cola = ColaFIFOConcurrente(4)


    for i in range(4):
        productor = Productor(cola, random.randint(1,1))
        consumidor = Consumidor(cola, random.randint(1,1))
        hilos.append(productor)
        hilos.append(consumidor)
        logging.info(f'Arrancando productor {productor.name}')
        productor.start()
        logging.info(f'Arrancando consumidor {consumidor.name}')
        consumidor.start()

    for thr in hilos:
        thr.join()

if __name__ == '__main__':
    main()

