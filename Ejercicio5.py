
import threading
import time
import random
import logging

from Ejercicio3b import ColaFIFOExtendida

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

lock = threading.Lock()

class Productor(threading.Thread):
    def __init__(self, cola, retardo):
        super().__init__()
        self.cola = cola
        self.retardo = retardo

    def run(self):
        while True:
            lock.acquire()
            self.cola.insertar(random.randint(0,100))
            try:
                logging.info(f'esta produciendo {self.cola.ultimo()}')
            finally:
                lock.release()
            time.sleep(self.retardo)


class Consumidor(threading.Thread):
    def __init__(self, cola, retardo):
        super().__init__()
        self.cola = cola
        self.retardo = retardo

    def run(self):
        while True:
            lock.acquire()
            try:
                elemento = self.cola.extraer()
                logging.info(f'consumio el elemento {elemento}')
            finally:
                lock.release()
            time.sleep(self.retardo)


def main():
    hilos = []
    cola = ColaFIFOExtendida(5)


    for i in range(1):
        productor = Productor(cola, random.randint(1,1))
        consumidor = Consumidor(cola, random.randint(2,2))
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
