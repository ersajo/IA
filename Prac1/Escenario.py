import pygame, time
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
        GRIS = (192, 192, 192)
        MELON = (255, 255, 153)
        AZUL = (0, 172, 230)
        AMARILLO = (255, 204, 0)
        VERDE = (46, 184, 46)
        NEGRO = (0, 0, 0)
        X = 0
        Y = 0
        for line in contenido:
            for car in line:
                if car == '0':
                    pygame.draw.rect(self.Pantalla, GRIS, [X,Y,50,50], 0)
                elif car == '1':
                    pygame.draw.rect(self.Pantalla, MELON, [X,Y,50,50], 0)
                elif car == '2':
                    pygame.draw.rect(self.Pantalla, AZUL, [X,Y,50,50], 0)
                elif car == '3':
                    pygame.draw.rect(self.Pantalla, AMARILLO, [X,Y,50,50], 0)
                elif car == '4':
                    pygame.draw.rect(self.Pantalla, VERDE, [X,Y,50,50], 0)
                elif car == -1:
                    pygame.draw.rect(self.Pantalla, NEGRO, [X,Y,50,50], 0)
                X = X + 50
            Y = Y + 50
            X = 0

    def getSombra(self):
        return self.Sombra

    def askTerrain(self):
        pos = pygame.mouse.get_pos()
        Num = self.World[pos[1]/50][pos[0]/50]
        myfont = pygame.font.SysFont("monospace bold", 30)
        if Num == '0':
            label = myfont.render("Mountain", 1, (244,110,120))
        elif Num == '1':
            label = myfont.render("Earth", 1, (244,110,120))
        elif Num == '2':
            label = myfont.render("Water", 1, (244,110,120))
        elif Num == '3':
            label = myfont.render("Sand", 1, (244,110,120))
        elif Num == '4':
            label = myfont.render("Forest", 1, (244,110,120))
        self.Pantalla.blit(label, (pos[0], pos[1]))

    def changeTerrain(self):
        pos = pygame.mouse.get_pos()
        print "Type:"
        print "0 -> Mountain"
        print "1 -> Earth"
        print "2 -> Water"
        print "3 -> Sand"
        print "4 -> Forest"
        terreno  = raw_input ("Write the number of the terrain type >>")
        self.World[pos[1]/50][pos[0]/50] = terreno
        self.Sombra[pos[1]/50][pos[0]/50] = terreno

    def getPos(self,charX,charY):
        return self.World[charY][charX]

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
                if fila != x:
                    World = World + random.randrange(6)+','
                else:
                    World = World + random.randrange(6)
