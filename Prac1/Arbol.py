from collections import deque

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

    def agregarElemento(self, arbol, elemento, elementoPadre):
        subarbol = self.buscarSubarbol(arbol, elementoPadre);
        subarbol.hijos.append(Arbol(elemento))

    def printElement(self, element):
        print element

    def buscarSubarbol(self, arbol, elemento):
        if arbol.elemento == elemento:
            return arbol
        for subarbol in arbol.hijos:
            arbolBuscado = self.buscarSubarbol(subarbol, elemento)
            if (arbolBuscado != None):
                return arbolBuscado
        return None

    def profundidad(self, arbol):
        if len(arbol.hijos) == 0:
            return 1
        return 1 + max(map(self.profundidad,arbol.hijos))

    def grado(self, arbol):
        return max(map(self.grado, arbol.hijos) + [len(arbol.hijos)])

    def ejecutarProfundidadPrimero(self, arbol, funcion):
        funcion(arbol.elemento)
        for hijo in arbol.hijos:
            self.ejecutarProfundidadPrimero(hijo, funcion)

    def ejecutarAnchoPrimero(self, arbol, funcion, cola = deque()):
        funcion(arbol.elemento)
        if (len(arbol.hijos) > 0):
            cola.extend(arbol.hijos)
        if (len(cola) != 0):
            self.ejecutarAnchoPrimero(cola.popleft(), funcion, cola)
