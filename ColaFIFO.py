"""
Ejemplo de Libería Impementando una cola FIFO de tamaño infinito

"""


class ColaFIFO:

    def __init__(self):
        self.elementos = []
        self.cola_vacia = True

    def insertar(self, dato):
        self.elementos.append(dato)
        self.cola_vacia = self.esta_vacia()
        return dato

    def extraer(self):
        elemento = self.elementos.pop(0)
        self.cola_vacia = self.esta_vacia()
        return elemento

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFO()

    # check if esta_vacia()

    print(cola.esta_vacia())

    for i in range (1,6):
        cola.insertar(i)

    print(cola.cola_vacia)
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia)
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()
