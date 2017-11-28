class Character:

    tipo = ""
    distancia = 0
    costos = []
    costoT = 0
    X = 0
    Y = 0
    Arbol =Arbol("0,0")


    def __init__(self, tipo, X, Y, costos):
        self.tipo = tipo
        self.X = X
        self.Y = Y
        arbol=Arbol(str(X)+","+str(Y))
        for i in range(len(costos)):
            if costos[i][0] == tipo:
                self.costos = costos[i]
                break

    @property
    def getX(self):
        return self.X

    @property
    def getY(self):
        return self.Y

    @property
    def getCostoT(self):
        return self.costoT

    @property
    def getcostos(self):
        return self.costos

    def askMove(self, mapa):
        return self.costos[int(mapa) + 1]

    def UP(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.Y = self.Y-50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def DOWN(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.Y = self.Y+50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def RIGHT(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.X = self.X+50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def LEFT(self, mapa, flag):
        if(mapa != False):
            if self.costos[int(mapa) + 1] != 'X':
                if flag == 1:
                    self.X = self.X-50
                    self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
                elif flag == 0:
                    return 0
            return 1

    def choice(self):
