import pygame
from Archivo import *
class Escenario:

    Dimensiones = (750,900)
    Pantalla = pygame.display.set_mode(Dimensiones)
    World = []
    Sombra = []

    def __init__(self,viewX, viewY):
        self.Dimensiones = (viewX*50, viewY*50)
        Pantalla = pygame.display.set_mode(self.Dimensiones)
        pygame.draw.rect(Pantalla, (255, 0, 255), [0,0,50,50], 0)

    def repaintCharacter(self, X, Y, color):
        pygame.draw.rect(self.Pantalla, color, [X,Y,50,50], 0)
        self.Sombra[Y/50][X/50] = self.World[Y/50][X/50]

        if (X/50 != 0):
            self.Sombra[Y/50][(X/50)-1] = self.World[Y/50][(X/50)-1]

        if (Y/50 != 0):
            self.Sombra[(Y/50)-1][X/50] = self.World[(Y/50)-1][X/50]

        if ((X/50)+1 < self.Dimensiones[0]/50):
            self.Sombra[Y/50][(X/50)+1] = self.World[Y/50][(X/50)+1]

        if ((Y/50)+1 < self.Dimensiones[1]/50):
            self.Sombra[(Y/50)+1][X/50] = self.World[(Y/50)+1][X/50]

    def getDimensiones(self):
        return self.Dimensiones

    def copyWorld(self, viewX, viewY):
        self.Sombra = [[-1 for j in range(viewX)] for i in range(viewY)]

    def printArreglo(self):
        print self.World
        print self.Sombra

    def paintWorld(self, contenido, flag):
        if flag == 0:
            self.Sombra = contenido
        elif flag == 1:
            self.World = contenido
        VERDE = (0, 255, 0)
        AZUL = (0, 0, 255)
        BLANCO = (255, 255, 255)
        X = 0
        Y = 0
        for line in contenido:
            for car in line:
                if car == '0':
                    pygame.draw.rect(self.Pantalla, AZUL, [X,Y,50,50], 0)
                elif car == '1':
                    pygame.draw.rect(self.Pantalla, VERDE, [X,Y,50,50], 0)
                elif car == -1:
                    pygame.draw.rect(self.Pantalla, BLANCO, [X,Y,50,50], 0)
                X = X + 50
            Y = Y + 50
            X = 0

    def getSombra(self):
        return self.Sombra

    def askUP(self,charX,charY):
        return self.World[charY-1][charX]

    def askDOWN(self,charX,charY):
        return self.World[charY+1][charX]

    def askLEFT(self,charX,charY):
        return self.World[charY][charX-1]

    def askRIGHT(self,charX,charY):
        return self.World[charY][charX+1]

    def CreateWorld(self, x, y):
        for columna in y:
            for fila in x:
                if fila != x
                    World = World + random.randrange(6)+','
                else
                    World = World + random.randrange(6)
