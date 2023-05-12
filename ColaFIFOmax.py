"""
Ejemplo de Libería Impementando una cola FIFO de tamaño finito
"""
class ColaFIFOmax():

    def __init__(self, size):
        self.elementos = []
        self.cola_vacia = True
        self.cola_llena = False
        self.size = size

    def insertar(self, dato):
        if self.cola_llena:
            raise Exception('Esta intentando insertar en una cola llena!')
        else:
            self.elementos.append(dato)
            self.cola_vacia = self.esta_vacia()
            self.cola_llena = self.esta_llena()
            return dato

    def extraer(self):
        elemento = self.elementos.pop(0)
        self.cola_vacia = self.esta_vacia()
        self.cola_llena = self.esta_llena()
        return elemento

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def esta_llena(self):
        return len(self.elementos) == self.size

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFOmax(5)

    # check if esta_vacia()

    print(cola.cola_vacia)

    for i in range (1,6):
        cola.insertar(i)

    print(cola.esta_vacia())
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.esta_vacia())
    print(cola.cantidad_elementos())

    try:
        for k in range(1,7):
            cola.insertar(k)
    except:
        print("Ocurrio una excepcion")



if __name__ == '__main__':
    main()
