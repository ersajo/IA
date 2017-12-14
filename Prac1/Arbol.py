from collections import deque

class Arbol:
    def __init__(self, elemento, padre, hoja ,profundidad):
        self.hijos = []
        self.elemento = elemento
        self.padre = padre
        self.hoja = hoja
        self.profundidad = profundidad

    def agregarElemento(self, arbol, elemento, elementoPadre,hoja,profundidad):
        subarbol = self.buscarSubarbol(arbol, elementoPadre)
        subarbol.hijos.append(Arbol(elemento,elementoPadre))

    def getFather(self,arbol,elemento):
        subarbol = self.buscarSubarbol(arbol, elemento)
        return subarbol.padre

    def removeElemento(self, arbol, elemento, elementoPadre):
        subarbol = self.buscarSubarbol(arbol, elementoPadre)
        subarbol.hijos.pop(2)

    def modificarElemento(self, arbol, elemento, elementoPadre):
        subarbol = self.buscarSubarbol(arbol, elementoPadre)
        subarbol.elemento = elemento

    def printElement(self, element,padre):
        print element+"-->"+padre
        return element

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
        el=funcion(arbol.elemento,arbol.padre)
        for hijo in arbol.hijos:
            self.ejecutarProfundidadPrimero(hijo, funcion)


    def ejecutarAnchoPrimero(self, arbol, funcion, cola = deque()):
        funcion(arbol.elemento)
        if (len(arbol.hijos) > 0):
            cola.extend(arbol.hijos)
        if (len(cola) != 0):
            self.ejecutarAnchoPrimero(cola.popleft(), funcion, cola)

#Tree=Arbol("0,0","0,0")

#Tree.agregarElemento(Tree,"1,0","0,0")
#Tree.agregarElemento(Tree, "2,0", "0,0")

#Tree.ejecutarProfundidadPrimero(Tree, Tree.printElement)
