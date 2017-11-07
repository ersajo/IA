class Character:

    tipo = ""
    distancia = 0
    costos = []
    costoT = 0
    X = 0
    Y = 0

    def __init__(self, tipo, X, Y, costos):
        self.tipo = tipo
        self.X = X
        self.Y = Y
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

    def UP(self, mapa):
        if self.costos[int(mapa) + 1] != 'X':
            self.Y = self.Y-50
            self.costoT = self.costoT + int(self.costos[int(mapa) + 1])

    def DOWN(self, mapa):
        if self.costos[int(mapa) + 1] != 'X':
            self.Y = self.Y+50
            self.costoT = self.costoT + int(self.costos[int(mapa) + 1])

    def RIGHT(self, mapa):
        if self.costos[int(mapa) + 1] != 'X':
            self.X = self.X+50
            self.costoT = self.costoT + int(self.costos[int(mapa) + 1])

    def LEFT(self, mapa):
        if self.costos[int(mapa) + 1] != 'X':
            self.X = self.X-50
            self.costoT = self.costoT + int(self.costos[int(mapa) + 1])
