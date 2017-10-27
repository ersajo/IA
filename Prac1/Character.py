class Character:

    tipo = "Monito"
    distancia = 0
    costo = 0
    X = 0
    Y = 0

    def __init__(self, tipo, X, Y):
        self.tipo = tipo
        self.X = X
        self.Y = Y

    @property
    def getX(self):
        return self.X

    @property
    def getY(self):
        return self.Y

    def UP(self):
        self.Y = self.Y-50

    def DOWN(self):
        self.Y = self.Y+50

    def RIGHT(self):
        self.X = self.X+50

    def LEFT(self):
        self.X = self.X-50
